/*
 Navicat Premium Data Transfer

 Source Server         : MySQL5.7
 Source Server Type    : MySQL
 Source Server Version : 50733
 Source Host           : localhost:3306
 Source Schema         : bank

 Target Server Type    : MySQL
 Target Server Version : 50733
 File Encoding         : 65001

 Date: 06/08/2021 14:41:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `userpassword` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `nat` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `pro` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `street` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `hnum` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `money` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('张四', '123456', '中国', '北京市昌平区', '七马路', '5号', '12345612346', '1000');
INSERT INTO `user` VALUES ('张三', '123456', '中国', '北京市昌平区', '七马路', '5号', '12345612345', '120');
INSERT INTO `user` VALUES ('11', '2', '2', '2', '2', '2', '45112936605', '0');
INSERT INTO `user` VALUES ('1', '1', '1', '1', '1', '1', '25474016078', '0');
INSERT INTO `user` VALUES ('3', '3', '3', '3', '3', '3', '60637001516', '31');
INSERT INTO `user` VALUES ('z', '123', 'a', 's', 'd', 'f', '74963349814', '0');
INSERT INTO `user` VALUES ('a', 'sda', 'ds', 'd', 's', 'f', '26348044468', '0');

SET FOREIGN_KEY_CHECKS = 1;
