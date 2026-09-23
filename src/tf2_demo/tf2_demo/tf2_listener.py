#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import tf2_ros

class TF2Listener(Node):
    def __init__(self):
        super().__init__('tf2_listener')
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(1.0, self.lookup_transform)

    def lookup_transform(self):
        try:
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                'laser_link',
                rclpy.time.Time()
            )
            translation = transform.transform.translation
            rotation = transform.transform.rotation
            self.get_logger().info(
                f'Translation: '
                f'x={translation.x:.3f}, '
                f'y={translation.y:.3f}, '
                f'z={translation.z:.3f}'
            )
            self.get_logger().info(
                f'Rotation: '
                f'x={rotation.x:.3f}, '
                f'y={rotation.y:.3f}, '
                f'z={rotation.z:.3f}, '
                f'w={rotation.w:.3f}'
            )

        except tf2_ros.LookupException:
            self.get_logger().warn('Transform not available yet.')

        except tf2_ros.ConnectivityException:
            self.get_logger().warn('TF connectivity error.')

        except tf2_ros.ExtrapolationException:
            self.get_logger().warn('TF extrapolation error.')

def main(args=None):
    rclpy.init(args=args)
    node = TF2Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()