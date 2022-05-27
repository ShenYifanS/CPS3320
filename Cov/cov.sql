/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50727
 Source Host           : localhost:3306
 Source Schema         : cov

 Target Server Type    : MySQL
 Target Server Version : 50727
 File Encoding         : 65001

 Date: 15/01/2022 22:22:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

use cov;
create database if not exists cov;

-- ----------------------------
-- Table structure for details
-- ----------------------------
DROP TABLE IF EXISTS `details`;
CREATE TABLE `details`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `update_time` datetime(0) DEFAULT NULL COMMENT '数据最后更新时间',
  `province` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '省',
  `city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '市',
  `confirm` int(10) DEFAULT NULL COMMENT '累计确诊',
  `confirm_add` int(10) DEFAULT NULL COMMENT '新增确诊',
  `confirm_now` int(10) DEFAULT NULL COMMENT '现有确诊',
  `heal` int(10) DEFAULT NULL COMMENT '累计治愈',
  `dead` int(10) DEFAULT NULL COMMENT '累计死亡',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2845 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history`  (
  `ds` datetime(0) NOT NULL COMMENT '日期',
  `confirm` int(10) DEFAULT NULL COMMENT '累计确诊',
  `confirm_add` int(10) DEFAULT NULL COMMENT '当日新增确诊',
  `confirm_now` int(10) DEFAULT NULL COMMENT '剩余确诊',
  `suspect` int(10) DEFAULT NULL COMMENT '剩余疑似',
  `suspect_add` int(10) DEFAULT NULL COMMENT '当日新增疑似',
  `heal` int(10) DEFAULT NULL COMMENT '累计治愈',
  `heal_add` int(10) DEFAULT NULL COMMENT '当日新增治愈',
  `dead` int(10) DEFAULT NULL COMMENT '累计死亡',
  `dead_add` int(10) DEFAULT NULL COMMENT '当日新增死亡',
  PRIMARY KEY (`ds`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hotsearch
-- ----------------------------
DROP TABLE IF EXISTS `hotsearch`;
CREATE TABLE `hotsearch`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `dt` datetime(0) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 331 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for risk_area
-- ----------------------------
DROP TABLE IF EXISTS `risk_area`;
CREATE TABLE `risk_area`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `end_update_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '数据最后更新时间',
  `province` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '省',
  `city` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '市',
  `county` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '县',
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '详细地址',
  `type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '风险类型',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 362 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
