/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : fflow

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-04-12 00:03:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  CONSTRAINT `auth_permission_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add user to user message', '1', 'add_usertousermessage');
INSERT INTO `auth_permission` VALUES ('2', 'Can change user to user message', '1', 'change_usertousermessage');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete user to user message', '1', 'delete_usertousermessage');
INSERT INTO `auth_permission` VALUES ('4', 'Can add system to user message', '2', 'add_systemtousermessage');
INSERT INTO `auth_permission` VALUES ('5', 'Can change system to user message', '2', 'change_systemtousermessage');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete system to user message', '2', 'delete_systemtousermessage');
INSERT INTO `auth_permission` VALUES ('7', 'Can add event message', '3', 'add_eventmessage');
INSERT INTO `auth_permission` VALUES ('8', 'Can change event message', '3', 'change_eventmessage');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete event message', '3', 'delete_eventmessage');
INSERT INTO `auth_permission` VALUES ('10', 'Can add add model', '4', 'add_addmodel');
INSERT INTO `auth_permission` VALUES ('11', 'Can change add model', '4', 'change_addmodel');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete add model', '4', 'delete_addmodel');
INSERT INTO `auth_permission` VALUES ('13', 'Can add post model', '5', 'add_postmodel');
INSERT INTO `auth_permission` VALUES ('14', 'Can change post model', '5', 'change_postmodel');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete post model', '5', 'delete_postmodel');
INSERT INTO `auth_permission` VALUES ('16', 'Can add comment', '6', 'add_comment');
INSERT INTO `auth_permission` VALUES ('17', 'Can change comment', '6', 'change_comment');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete comment', '6', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('19', 'Can add class', '7', 'add_class');
INSERT INTO `auth_permission` VALUES ('20', 'Can change class', '7', 'change_class');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete class', '7', 'delete_class');
INSERT INTO `auth_permission` VALUES ('22', 'Can add thread', '8', 'add_thread');
INSERT INTO `auth_permission` VALUES ('23', 'Can change thread', '8', 'change_thread');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete thread', '8', 'delete_thread');
INSERT INTO `auth_permission` VALUES ('25', 'Can add tag', '9', 'add_tag');
INSERT INTO `auth_permission` VALUES ('26', 'Can change tag', '9', 'change_tag');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete tag', '9', 'delete_tag');
INSERT INTO `auth_permission` VALUES ('28', 'Can add user profile', '10', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('29', 'Can change user profile', '10', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete user profile', '10', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('31', 'Can add log entry', '11', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('32', 'Can change log entry', '11', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete log entry', '11', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('34', 'Can add permission', '12', 'add_permission');
INSERT INTO `auth_permission` VALUES ('35', 'Can change permission', '12', 'change_permission');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete permission', '12', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('37', 'Can add group', '13', 'add_group');
INSERT INTO `auth_permission` VALUES ('38', 'Can change group', '13', 'change_group');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete group', '13', 'delete_group');
INSERT INTO `auth_permission` VALUES ('40', 'Can add user', '14', 'add_user');
INSERT INTO `auth_permission` VALUES ('41', 'Can change user', '14', 'change_user');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete user', '14', 'delete_user');
INSERT INTO `auth_permission` VALUES ('43', 'Can add content type', '15', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('44', 'Can change content type', '15', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete content type', '15', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('46', 'Can add session', '16', 'add_session');
INSERT INTO `auth_permission` VALUES ('47', 'Can change session', '16', 'change_session');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete session', '16', 'delete_session');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 帖子类型', '17', 'add_subclass');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 帖子类型', '17', 'change_subclass');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 帖子类型', '17', 'delete_subclass');
INSERT INTO `auth_permission` VALUES ('52', 'Can add comment', '18', 'add_comment');
INSERT INTO `auth_permission` VALUES ('53', 'Can change comment', '18', 'change_comment');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete comment', '18', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('55', 'Can add system email info', '19', 'add_systememailinfo');
INSERT INTO `auth_permission` VALUES ('56', 'Can change system email info', '19', 'change_systememailinfo');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete system email info', '19', 'delete_systememailinfo');
INSERT INTO `auth_permission` VALUES ('58', 'Can add user summer', '20', 'add_usersummer');
INSERT INTO `auth_permission` VALUES ('59', 'Can change user summer', '20', 'change_usersummer');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete user summer', '20', 'delete_usersummer');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$30000$KfO4Gh9NksAs$foR9ECGRViVeyQVtUy12N59fMpv4IaYMbDItaDXaE1o=', '2017-03-04 01:04:06', '1', 'none', '', '', 'none@example.com', '1', '1', '2017-03-03 13:45:28');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$30000$a0Wt9R9rF2Lq$PN3RMty/dNaAy3bNvsTaC4KZ5c4K+9Hf68OF0Z/HmB4=', '2017-04-11 14:32:11', '1', 'admin', '管理员是我爸爸', '我是', 'admin@example.com', '1', '1', '2017-03-03 13:46:24');
INSERT INTO `auth_user` VALUES ('3', 'password', null, '0', 'username', '', '', '', '0', '1', '2017-03-03 15:39:37');
INSERT INTO `auth_user` VALUES ('4', 'pbkdf2_sha256$30000$jlx8heHH5x1D$We+WeJFmrLMUaO47QbtCJraw5To99VrQ7/eB4QsSlcs=', null, '0', 'user0098', '', '', 'kk@qq.com', '0', '1', '2017-03-04 01:00:34');
INSERT INTO `auth_user` VALUES ('5', 'pbkdf2_sha256$30000$8ejPhpUg0BDu$Ppxs55G/b4SiA/37FDqDyrnlfnWe6Zn/I8626gvJWuQ=', null, '0', 'woshi', '', '', 'kk@qq.com', '0', '1', '2017-03-04 01:03:13');
INSERT INTO `auth_user` VALUES ('6', 'pbkdf2_sha256$30000$5Qshwbpfkpmx$VBAzur3mhWZeWognNKqs4qfjbxXLV9CXTadlj6/KjJU=', null, '0', 'user00999', '', '', 'kk@qq.com', '0', '1', '2017-03-04 01:03:47');
INSERT INTO `auth_user` VALUES ('7', 'pbkdf2_sha256$30000$bpTxPhC6YxK4$IZa44O+FfgZaTWJAEGPJrBVBGWFGaRzXYAlZS4aUtec=', '2017-04-11 01:09:47', '0', 'taita', '', '', 'taita@gmail.com', '0', '1', '2017-03-04 01:14:32');
INSERT INTO `auth_user` VALUES ('8', 'pbkdf2_sha256$30000$VusGetCV584w$pu4Jo7WtDaa3nnESQxBYMGmqEITTV2F8+9Iqa42QY1s=', '2017-03-04 02:14:37', '0', 'mmix', '', '', 'mmix@gmail.com', '0', '1', '2017-03-04 02:14:29');
INSERT INTO `auth_user` VALUES ('9', 'pbkdf2_sha256$30000$RRn77Kx9Zu5x$CpLnoMYR5ZukcZMfLzPaP4DN5+PKX8p3eEEcAdKhhnY=', '2017-03-04 05:36:30', '0', 'dgut', '', '', 'uu@qq.com', '0', '1', '2017-03-04 05:36:21');
INSERT INTO `auth_user` VALUES ('10', 'pbkdf2_sha256$30000$qzotbKQXH4nw$GbDDU7KBOPg1JOtfEwN4I/uhTs2fPGw6EUCqq0PkJBM=', '2017-03-04 05:38:41', '0', 'woshidashabi', '', '', 'kk@qq.com', '0', '1', '2017-03-04 05:38:35');
INSERT INTO `auth_user` VALUES ('11', 'pbkdf2_sha256$30000$GqKIvnE6mbBr$WM3yHt8HkVMlaMNUIdbxlSvGManuok9+TdOqFF7LpAQ=', '2017-04-07 07:25:13', '0', 'adminn', 'ddrff', '', 'test1@qq.com', '0', '1', '2017-04-06 13:00:01');
INSERT INTO `auth_user` VALUES ('12', 'pbkdf2_sha256$30000$gReVAwznfApJ$YCFw9YrkvmQZYa1d6cFe/jwHmDumx4w53YzKhIJV/Ws=', '2017-04-07 07:37:26', '0', 'test2', 'hiash', '', 'test2@qq.com', '0', '1', '2017-04-07 07:35:50');
INSERT INTO `auth_user` VALUES ('13', 'pbkdf2_sha256$30000$byXaOoMYHopg$GDq2V2InCTydqrQbg6lxNFNDzBXnKAg/KE1gNGkQsfc=', '2017-04-11 14:23:47', '0', 'll', '', '', 'll@qq.com', '0', '1', '2017-04-11 14:23:41');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`) USING BTREE,
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`) USING BTREE,
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2017-04-07 07:24:35', '1', 'Comment object', '1', '[{\"added\": {}}]', '6', '2');
INSERT INTO `django_admin_log` VALUES ('2', '2017-04-07 07:29:38', '2', 'Comment object', '1', '[{\"added\": {}}]', '6', '2');
INSERT INTO `django_admin_log` VALUES ('3', '2017-04-08 09:06:29', '1', 'Class object', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('4', '2017-04-08 13:53:35', '2', 'Class object', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('5', '2017-04-08 13:53:46', '3', 'Class object', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('6', '2017-04-08 13:53:54', '1', 'Class object', '3', '', '7', '2');
INSERT INTO `django_admin_log` VALUES ('7', '2017-04-08 13:54:12', '4', 'Class object', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('8', '2017-04-08 13:54:22', '5', 'Class object', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('9', '2017-04-08 13:55:25', '1', 'JavaScript', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('10', '2017-04-08 13:55:31', '2', 'Python', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('11', '2017-04-08 13:55:38', '3', 'PHP', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('12', '2017-04-09 01:54:40', '1', 'Thread object', '1', '[{\"added\": {}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('13', '2017-04-09 07:04:40', '3', 'taita--ll--我今天吃了', '1', '[{\"added\": {}}]', '6', '2');
INSERT INTO `django_admin_log` VALUES ('14', '2017-04-09 12:20:08', '16', 'sadasdsdfdg', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('15', '2017-04-09 12:20:08', '15', 'sss', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('16', '2017-04-09 12:20:08', '14', 'sss', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('17', '2017-04-09 12:20:08', '13', 'sdsds', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('18', '2017-04-09 12:20:08', '12', 'sdsd', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('19', '2017-04-09 12:20:08', '11', 'ss', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('20', '2017-04-09 12:20:08', '10', 'hishshasdghhkoyuitwerewr', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('21', '2017-04-09 12:30:47', '34', 'asd', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('22', '2017-04-09 12:30:47', '33', 'asdasda', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('23', '2017-04-09 12:30:47', '32', 'asdasdas', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('24', '2017-04-09 12:30:47', '31', 'asdasdas', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('25', '2017-04-09 12:30:47', '30', 'asdasdas', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('26', '2017-04-09 12:30:47', '29', 'asdasdas', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('27', '2017-04-09 12:30:47', '28', 'asdasdas', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('28', '2017-04-09 12:30:47', '27', 'asdasdas', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('29', '2017-04-09 12:30:47', '26', 'asdasdas', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('30', '2017-04-09 12:30:47', '25', 'asdadsfsdg', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('31', '2017-04-09 12:30:47', '24', 'dfsdf', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('32', '2017-04-09 12:30:47', '23', 'dfsdf', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('33', '2017-04-09 12:30:47', '22', 'dfsdf', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('34', '2017-04-09 12:30:47', '21', 'asdhdgfhfjug', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('35', '2017-04-09 12:30:47', '20', 'sdasd', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('36', '2017-04-09 12:30:47', '19', 'asdasda', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('37', '2017-04-09 12:30:47', '18', 'sdsad', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('38', '2017-04-09 12:30:47', '17', 'asdasdadsa', '3', '', '6', '2');
INSERT INTO `django_admin_log` VALUES ('39', '2017-04-10 05:34:36', '1', 'SystemToUserMessage object', '1', '[{\"added\": {}}]', '2', '2');
INSERT INTO `django_admin_log` VALUES ('40', '2017-04-10 05:48:56', '2', '编程语言', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('41', '2017-04-10 05:49:00', '4', '交易', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('42', '2017-04-10 05:49:04', '3', '城市', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('43', '2017-04-10 05:56:24', '6', 'funny', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('44', '2017-04-10 05:56:45', '5', 'technique', '2', '[{\"changed\": {\"fields\": [\"name\", \"display_name\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('45', '2017-04-10 05:56:53', '2', 'programming', '2', '[{\"changed\": {\"fields\": [\"name\", \"display_name\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('46', '2017-04-10 05:58:24', '4', 'transaction', '2', '[{\"changed\": {\"fields\": [\"name\", \"display_name\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('47', '2017-04-10 05:58:31', '3', 'city', '2', '[{\"changed\": {\"fields\": [\"name\", \"display_name\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('48', '2017-04-10 06:00:06', '7', '', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('49', '2017-04-10 06:00:23', '7', '营销', '2', '[{\"changed\": {\"fields\": [\"name\", \"display_name\", \"create_user\", \"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('50', '2017-04-10 06:00:44', '8', '设计', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('51', '2017-04-10 06:01:21', '9', '数码', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('52', '2017-04-10 06:01:26', '5', '技术', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('53', '2017-04-10 06:01:33', '2', '编程语言', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('54', '2017-04-10 06:01:38', '4', '交易', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('55', '2017-04-10 06:01:43', '3', '城市', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('56', '2017-04-10 06:01:46', '6', '好玩', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('57', '2017-04-10 06:01:50', '7', '营销', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('58', '2017-04-10 06:01:53', '8', '设计', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('59', '2017-04-10 06:01:59', '9', '数码', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('60', '2017-04-10 06:02:52', '10', '生活', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('61', '2017-04-10 06:15:41', '11', '更多', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('62', '2017-04-10 07:10:50', '4', 'cloud-computing', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('63', '2017-04-10 07:12:20', '3', 'PHP', '2', '[{\"changed\": {\"fields\": [\"display_name\"]}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('64', '2017-04-10 07:12:35', '2', 'Python', '2', '[{\"changed\": {\"fields\": [\"display_name\"]}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('65', '2017-04-10 07:12:41', '1', 'JavaScript', '2', '[{\"changed\": {\"fields\": [\"display_name\"]}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('66', '2017-04-10 07:13:01', '3', 'PHP', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('67', '2017-04-10 07:13:07', '2', 'Python', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('68', '2017-04-10 07:13:12', '1', 'JavaScript', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('69', '2017-04-10 07:15:09', '5', '人工智能', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('70', '2017-04-10 07:15:47', '6', '深度学习', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('71', '2017-04-10 07:16:07', '7', '数据挖掘', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('72', '2017-04-10 07:16:43', '8', '计算机网络', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('73', '2017-04-10 08:40:39', '12', '职场', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('74', '2017-04-10 08:40:46', '12', '职场', '2', '[{\"changed\": {\"fields\": [\"order\"]}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('75', '2017-04-10 14:11:50', '13', '计算机基础', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('76', '2017-04-10 15:15:25', '13', '计算机基础', '3', '', '7', '2');
INSERT INTO `django_admin_log` VALUES ('77', '2017-04-10 15:15:25', '9', '数码', '3', '', '7', '2');
INSERT INTO `django_admin_log` VALUES ('78', '2017-04-11 01:12:52', '9', 'GO', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('79', '2017-04-11 07:14:57', '10', '跳槽', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('80', '2017-04-11 07:15:42', '11', '同事', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('81', '2017-04-11 07:16:15', '12', '转行', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('82', '2017-04-11 07:16:48', '13', 'C++', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('83', '2017-04-11 07:17:44', '14', '深圳', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('84', '2017-04-11 07:18:07', '15', '北京', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('85', '2017-04-11 07:18:20', '16', '广州', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('86', '2017-04-11 07:18:32', '17', '上海', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('87', '2017-04-11 07:18:49', '18', '杭州', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('88', '2017-04-11 07:19:39', '19', '租房', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('89', '2017-04-11 07:20:11', '20', '出行', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('90', '2017-04-11 07:21:31', '21', '打扮', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('91', '2017-04-11 07:22:43', '13', '带宽', '1', '[{\"added\": {}}]', '7', '2');
INSERT INTO `django_admin_log` VALUES ('92', '2017-04-11 07:45:19', '22', '交友', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('93', '2017-04-11 07:46:31', '23', '程序员', '1', '[{\"added\": {}}]', '17', '2');
INSERT INTO `django_admin_log` VALUES ('94', '2017-04-11 08:14:18', '1', '请问这个是什么', '2', '[{\"changed\": {\"fields\": [\"main_class\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('95', '2017-04-11 08:15:39', '1', '请问这个是什么', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('96', '2017-04-11 10:33:05', '2', '程序员的第一个贴子', '1', '[{\"added\": {}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('97', '2017-04-11 10:36:46', '2', '程序员的第一个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('98', '2017-04-11 10:37:20', '2', '程序员的第一个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('99', '2017-04-11 10:37:38', '1', '请问这个是什么', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('100', '2017-04-11 10:38:04', '1', '请问这个是什么', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('101', '2017-04-11 10:39:13', '1', '请问这个是什么', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('102', '2017-04-11 10:55:51', '2', '程序员的第一个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('103', '2017-04-11 10:56:13', '2', '程序员的第一个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('104', '2017-04-11 10:56:41', '2', '程序员的第一个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('105', '2017-04-11 10:57:36', '2', '程序员的第一个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('106', '2017-04-11 10:57:51', '2', '程序员的第一个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('107', '2017-04-11 10:58:23', '2', '程序员的第一个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('108', '2017-04-11 11:00:33', '3', '程序员的第二个贴子', '1', '[{\"added\": {}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('109', '2017-04-11 11:00:45', '3', '程序员的第二个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('110', '2017-04-11 11:00:51', '3', '程序员的第二个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('111', '2017-04-11 11:03:45', '4', '程序员的第三个贴子', '1', '[{\"added\": {}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('112', '2017-04-11 11:05:39', '4', '程序员的第三个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('113', '2017-04-11 11:05:57', '4', '程序员的第三个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('114', '2017-04-11 11:10:04', '4', '程序员的第三个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('115', '2017-04-11 11:11:22', '4', '程序员的第三个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('116', '2017-04-11 11:22:09', '4', '程序员的第三个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('117', '2017-04-11 11:22:56', '4', '程序员的第三个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('118', '2017-04-11 11:23:29', '4', '程序员的第三个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('119', '2017-04-11 11:27:54', '4', '程序员的第三个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('120', '2017-04-11 11:28:17', '4', '程序员的第三个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('121', '2017-04-11 11:29:20', '4', '程序员的第三个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('122', '2017-04-11 11:29:57', '4', '程序员的第三个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('123', '2017-04-11 11:32:16', '4', '程序员的第三个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('124', '2017-04-11 11:32:41', '4', '程序员的第三个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('125', '2017-04-11 11:33:14', '4', '程序员的第三个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('126', '2017-04-11 11:33:54', '4', '程序员的第三个贴子', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('127', '2017-04-11 11:34:03', '3', '程序员的第二个贴子', '2', '[]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('128', '2017-04-11 12:53:27', '5', '你好,世界', '1', '[{\"added\": {}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('129', '2017-04-11 12:58:46', '6', '如果硬盘被拆开如果被盗，会看到群晖里储存', '1', '[{\"added\": {}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('130', '2017-04-11 12:59:51', '6', '如果硬盘被拆开如果被盗，会看到群晖里储存的东西吗', '2', '[{\"changed\": {\"fields\": [\"tittle\"]}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('131', '2017-04-11 13:02:12', '7', '这是云计算的第一个贴子', '1', '[{\"added\": {}}]', '8', '2');
INSERT INTO `django_admin_log` VALUES ('132', '2017-04-11 16:02:13', '8', '中国人工智能产业数据图谱：55家医疗人工智能企业全扫描', '1', '[{\"added\": {}}]', '8', '2');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('11', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('13', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('12', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('14', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('15', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'forum', 'class');
INSERT INTO `django_content_type` VALUES ('18', 'forum', 'comment');
INSERT INTO `django_content_type` VALUES ('17', 'forum', 'subclass');
INSERT INTO `django_content_type` VALUES ('9', 'forum', 'tag');
INSERT INTO `django_content_type` VALUES ('8', 'forum', 'thread');
INSERT INTO `django_content_type` VALUES ('20', 'forum', 'usersummer');
INSERT INTO `django_content_type` VALUES ('10', 'index', 'userprofile');
INSERT INTO `django_content_type` VALUES ('4', 'lab', 'addmodel');
INSERT INTO `django_content_type` VALUES ('5', 'lab', 'postmodel');
INSERT INTO `django_content_type` VALUES ('3', 'message', 'eventmessage');
INSERT INTO `django_content_type` VALUES ('2', 'message', 'systemtousermessage');
INSERT INTO `django_content_type` VALUES ('1', 'message', 'usertousermessage');
INSERT INTO `django_content_type` VALUES ('16', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('19', 'setting', 'systememailinfo');
INSERT INTO `django_content_type` VALUES ('6', 'timeline', 'comment');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-02-24 06:09:01');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('13', 'sessions', '0001_initial', '2017-02-24 06:09:02');
INSERT INTO `django_migrations` VALUES ('14', 'music', '0001_initial', '2017-02-24 06:45:57');
INSERT INTO `django_migrations` VALUES ('15', 'music', '0002_music_is_good', '2017-02-24 07:09:52');
INSERT INTO `django_migrations` VALUES ('17', 'index', '0001_initial', '2017-02-24 14:09:56');
INSERT INTO `django_migrations` VALUES ('18', 'index', '0002_userprofile_avatar_path', '2017-02-27 02:59:38');
INSERT INTO `django_migrations` VALUES ('19', 'lab', '0001_initial', '2017-02-27 13:33:55');
INSERT INTO `django_migrations` VALUES ('20', 'lab', '0002_auto_20170227_2135', '2017-02-27 13:35:38');
INSERT INTO `django_migrations` VALUES ('21', 'lab', '0003_postmodel', '2017-02-28 02:22:32');
INSERT INTO `django_migrations` VALUES ('22', 'lab', '0004_auto_20170228_1025', '2017-02-28 02:25:52');
INSERT INTO `django_migrations` VALUES ('23', 'lab', '0005_postmodel_user', '2017-02-28 03:51:27');
INSERT INTO `django_migrations` VALUES ('26', 'index', '0003_userprofile_avatar', '2017-02-28 07:20:51');
INSERT INTO `django_migrations` VALUES ('27', 'index', '0004_auto_20170228_1522', '2017-02-28 07:23:05');
INSERT INTO `django_migrations` VALUES ('28', 'index', '0005_auto_20170228_1559', '2017-02-28 07:59:59');
INSERT INTO `django_migrations` VALUES ('29', 'index', '0006_userprofile_work_place', '2017-02-28 08:02:01');
INSERT INTO `django_migrations` VALUES ('30', 'index', '0007_auto_20170228_1619', '2017-02-28 08:19:57');
INSERT INTO `django_migrations` VALUES ('31', 'timeline', '0001_initial', '2017-02-28 11:14:42');
INSERT INTO `django_migrations` VALUES ('32', 'index', '0008_auto_20170228_2054', '2017-02-28 12:54:35');
INSERT INTO `django_migrations` VALUES ('33', 'index', '0009_auto_20170228_2130', '2017-02-28 13:30:18');
INSERT INTO `django_migrations` VALUES ('34', 'index', '0010_userprofile_sign', '2017-03-01 02:49:13');
INSERT INTO `django_migrations` VALUES ('35', 'message', '0001_initial', '2017-03-01 02:49:13');
INSERT INTO `django_migrations` VALUES ('36', 'index', '0011_auto_20170301_1050', '2017-03-01 02:50:58');
INSERT INTO `django_migrations` VALUES ('39', 'index', '0012_userprofile_set_avatar', '2017-03-03 13:44:19');
INSERT INTO `django_migrations` VALUES ('40', 'index', '0013_userprofile_work_year', '2017-03-04 02:11:56');
INSERT INTO `django_migrations` VALUES ('43', 'index', '0014_userprofile_blog_adderss', '2017-03-04 04:47:08');
INSERT INTO `django_migrations` VALUES ('44', 'index', '0015_auto_20170304_1333', '2017-03-04 05:34:50');
INSERT INTO `django_migrations` VALUES ('46', 'timeline', '0002_auto_20170408_0826', '2017-04-08 00:27:06');
INSERT INTO `django_migrations` VALUES ('47', 'forum', '0001_initial', '2017-04-08 09:05:51');
INSERT INTO `django_migrations` VALUES ('48', 'forum', '0002_auto_20170408_2307', '2017-04-08 15:07:50');
INSERT INTO `django_migrations` VALUES ('49', 'forum', '0003_thread_sub_class', '2017-04-09 01:53:39');
INSERT INTO `django_migrations` VALUES ('50', 'index', '0016_auto_20170409_0953', '2017-04-09 01:53:39');
INSERT INTO `django_migrations` VALUES ('51', 'forum', '0004_auto_20170409_1509', '2017-04-09 07:09:50');
INSERT INTO `django_migrations` VALUES ('52', 'timeline', '0003_remove_comment_tittle', '2017-04-09 08:12:49');
INSERT INTO `django_migrations` VALUES ('53', 'timeline', '0004_auto_20170409_1616', '2017-04-09 08:17:22');
INSERT INTO `django_migrations` VALUES ('54', 'index', '0017_auto_20170409_2033', '2017-04-09 12:33:21');
INSERT INTO `django_migrations` VALUES ('55', 'forum', '0005_auto_20170409_2246', '2017-04-09 14:47:03');
INSERT INTO `django_migrations` VALUES ('56', 'message', '0002_auto_20170409_2358', '2017-04-09 15:59:11');
INSERT INTO `django_migrations` VALUES ('57', 'message', '0003_auto_20170410_1033', '2017-04-10 02:33:30');
INSERT INTO `django_migrations` VALUES ('58', 'setting', '0001_initial', '2017-04-10 05:29:30');
INSERT INTO `django_migrations` VALUES ('59', 'forum', '0006_auto_20170410_1347', '2017-04-10 05:47:18');
INSERT INTO `django_migrations` VALUES ('60', 'forum', '0007_auto_20170410_1422', '2017-04-10 06:22:31');
INSERT INTO `django_migrations` VALUES ('61', 'forum', '0008_auto_20170410_1513', '2017-04-10 07:13:51');
INSERT INTO `django_migrations` VALUES ('62', 'forum', '0009_auto_20170410_1514', '2017-04-10 07:14:42');
INSERT INTO `django_migrations` VALUES ('63', 'forum', '0010_auto_20170411_1551', '2017-04-11 07:52:06');
INSERT INTO `django_migrations` VALUES ('64', 'forum', '0011_auto_20170411_1552', '2017-04-11 07:52:43');
INSERT INTO `django_migrations` VALUES ('65', 'forum', '0012_thread_main_class', '2017-04-11 07:54:38');
INSERT INTO `django_migrations` VALUES ('66', 'forum', '0013_usersummer', '2017-04-11 08:17:59');
INSERT INTO `django_migrations` VALUES ('67', 'forum', '0014_auto_20170411_1831', '2017-04-11 10:31:52');
INSERT INTO `django_migrations` VALUES ('68', 'forum', '0015_auto_20170411_1832', '2017-04-11 10:32:42');
INSERT INTO `django_migrations` VALUES ('69', 'forum', '0016_auto_20170411_1940', '2017-04-11 11:40:12');
INSERT INTO `django_migrations` VALUES ('70', 'forum', '0017_auto_20170411_2059', '2017-04-11 12:59:46');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('01vmip3fraoi41969qj2q6pu8qwinwww', 'ZDQwMmZkN2JiZDdjOWQzMjc0M2RiNjUyNGViMWVjNzA0NzA1ZGM5MTp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkODQ1MTgyYzQ5NzU4YTJjN2E1NzNmNjMzYTZmZDUxM2U3Y2JiNjFiIn0=', '2017-04-25 01:09:47');
INSERT INTO `django_session` VALUES ('1uib5ejlh2rb5t111yv7qg31qqmvcxit', 'OTBiODc2M2FjOTBjNTUyZjk1NDNiMDczMmZiOWZjNjY0ODBmMDMwNDp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmM5M2RkYjcwNmJiZjY2ODIyNTYwZTU2ZjQ2YWNhYTY2M2NmZjFiZCJ9', '2017-04-21 07:36:00');
INSERT INTO `django_session` VALUES ('8tzrta0131blnq573mwomow8upd8wj2z', 'N2FjNDI4NTJiMGYyNzM3NWFjZWI3NzM3MTAyNmNmNDc1OThiZjUxNzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxM2Y1NWFmNTY3ODcxOWZiOWU2N2UwZjI4NjM3MjFiN2E0MzYzYjFhIn0=', '2017-04-03 06:50:32');
INSERT INTO `django_session` VALUES ('fvf8m9d2qs0jnppc0as99wwrn8afeykr', 'N2FjNDI4NTJiMGYyNzM3NWFjZWI3NzM3MTAyNmNmNDc1OThiZjUxNzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxM2Y1NWFmNTY3ODcxOWZiOWU2N2UwZjI4NjM3MjFiN2E0MzYzYjFhIn0=', '2017-04-25 14:32:11');
INSERT INTO `django_session` VALUES ('lw7rblukf2pe691urzc6qcclprdexydv', 'N2FjNDI4NTJiMGYyNzM3NWFjZWI3NzM3MTAyNmNmNDc1OThiZjUxNzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxM2Y1NWFmNTY3ODcxOWZiOWU2N2UwZjI4NjM3MjFiN2E0MzYzYjFhIn0=', '2017-04-23 14:22:52');
INSERT INTO `django_session` VALUES ('m3c22wdiz7daalh0j6l6ae07e818qasc', 'N2FjNDI4NTJiMGYyNzM3NWFjZWI3NzM3MTAyNmNmNDc1OThiZjUxNzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxM2Y1NWFmNTY3ODcxOWZiOWU2N2UwZjI4NjM3MjFiN2E0MzYzYjFhIn0=', '2017-04-23 02:06:32');
INSERT INTO `django_session` VALUES ('o1prumc323bjijjv91s1yzqvr8w2uid8', 'N2FjNDI4NTJiMGYyNzM3NWFjZWI3NzM3MTAyNmNmNDc1OThiZjUxNzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxM2Y1NWFmNTY3ODcxOWZiOWU2N2UwZjI4NjM3MjFiN2E0MzYzYjFhIn0=', '2017-04-23 04:58:52');
INSERT INTO `django_session` VALUES ('t8h6txbc8yod8ylbnt0fztsyo76ngpbq', 'N2FjNDI4NTJiMGYyNzM3NWFjZWI3NzM3MTAyNmNmNDc1OThiZjUxNzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxM2Y1NWFmNTY3ODcxOWZiOWU2N2UwZjI4NjM3MjFiN2E0MzYzYjFhIn0=', '2017-04-24 10:29:55');
INSERT INTO `django_session` VALUES ('ulsclz23qdys7en4gn7fvaehagejqykr', 'N2FjNDI4NTJiMGYyNzM3NWFjZWI3NzM3MTAyNmNmNDc1OThiZjUxNzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxM2Y1NWFmNTY3ODcxOWZiOWU2N2UwZjI4NjM3MjFiN2E0MzYzYjFhIn0=', '2017-03-31 14:38:39');

-- ----------------------------
-- Table structure for forum_class
-- ----------------------------
DROP TABLE IF EXISTS `forum_class`;
CREATE TABLE `forum_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `last_time` datetime(6) DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `display_name` varchar(50) DEFAULT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_class_create_user_id_3e1448d5_fk_auth_user_id` (`create_user_id`),
  CONSTRAINT `forum_class_create_user_id_3e1448d5_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of forum_class
-- ----------------------------
INSERT INTO `forum_class` VALUES ('2', 'programming', '2017-04-10 06:01:33.445287', '2017-04-08 13:53:35.979173', '2', '编程语言', '20');
INSERT INTO `forum_class` VALUES ('3', 'city', '2017-04-10 06:01:43.002993', '2017-04-08 13:53:46.049389', '2', '城市', '40');
INSERT INTO `forum_class` VALUES ('4', 'transaction', '2017-04-10 06:01:38.990000', '2017-04-08 13:54:12.478773', '2', '交易', '30');
INSERT INTO `forum_class` VALUES ('5', 'technique', '2017-04-10 06:01:26.291826', '2017-04-08 13:54:22.022383', '2', '技术', '10');
INSERT INTO `forum_class` VALUES ('6', 'funny', '2017-04-10 06:01:46.812330', '2017-04-10 05:56:24.489458', '2', '好玩', '50');
INSERT INTO `forum_class` VALUES ('7', 'marketing', '2017-04-10 06:01:50.347710', '2017-04-10 06:00:06.950018', '2', '营销', '80');
INSERT INTO `forum_class` VALUES ('8', 'design', '2017-04-10 06:01:53.764591', '2017-04-10 06:00:44.795783', '2', '设计', '90');
INSERT INTO `forum_class` VALUES ('10', 'living', '2017-04-10 06:02:52.414126', '2017-04-10 06:02:52.414126', '2', '生活', '11');
INSERT INTO `forum_class` VALUES ('11', 'more', '2017-04-10 06:15:41.284998', '2017-04-10 06:15:41.284998', '2', '更多', '9999');
INSERT INTO `forum_class` VALUES ('12', 'career-spot', '2017-04-10 08:40:46.613725', '2017-04-10 08:40:39.300996', '2', '职场', '13');
INSERT INTO `forum_class` VALUES ('13', 'bandwidth', '2017-04-11 07:22:43.295655', '2017-04-11 07:22:43.295655', '2', '带宽', '200');

-- ----------------------------
-- Table structure for forum_comment
-- ----------------------------
DROP TABLE IF EXISTS `forum_comment`;
CREATE TABLE `forum_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thread_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_comment_thread_id_9cc3073e_fk_forum_thread_id` (`thread_id`),
  CONSTRAINT `forum_comment_thread_id_9cc3073e_fk_forum_thread_id` FOREIGN KEY (`thread_id`) REFERENCES `forum_thread` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of forum_comment
-- ----------------------------

-- ----------------------------
-- Table structure for forum_subclass
-- ----------------------------
DROP TABLE IF EXISTS `forum_subclass`;
CREATE TABLE `forum_subclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `last_time` datetime(6) NOT NULL,
  `create_user_id` int(11) NOT NULL,
  `parent_class_id` int(11) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_subclass_create_user_id_6f56201b_fk_auth_user_id` (`create_user_id`),
  KEY `forum_subclass_parent_class_id_90da0dd4_fk_forum_class_id` (`parent_class_id`),
  CONSTRAINT `forum_subclass_create_user_id_6f56201b_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `forum_subclass_parent_class_id_90da0dd4_fk_forum_class_id` FOREIGN KEY (`parent_class_id`) REFERENCES `forum_class` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of forum_subclass
-- ----------------------------
INSERT INTO `forum_subclass` VALUES ('1', 'javascript', '2017-04-10 07:13:12.829340', '2017-04-08 13:55:25.138438', '2', '2', 'JavaScript', '1');
INSERT INTO `forum_subclass` VALUES ('2', 'python', '2017-04-10 07:13:07.178588', '2017-04-08 13:55:31.771265', '2', '2', 'Python', '1');
INSERT INTO `forum_subclass` VALUES ('3', 'php', '2017-04-10 07:13:01.572701', '2017-04-08 13:55:38.772983', '2', '2', 'PHP', '1');
INSERT INTO `forum_subclass` VALUES ('4', 'cloud-computing', '2017-04-10 07:10:50.165516', '2017-04-10 07:10:50.165516', '2', '5', '云计算', '10');
INSERT INTO `forum_subclass` VALUES ('5', 'artifiaicl-intennigence', '2017-04-10 07:15:09.820398', '2017-04-10 07:15:09.820398', '2', '5', '人工智能', '20');
INSERT INTO `forum_subclass` VALUES ('6', 'deep-learning', '2017-04-10 07:15:47.671007', '2017-04-10 07:15:47.671007', '2', '5', '深度学习', '30');
INSERT INTO `forum_subclass` VALUES ('7', 'data-mining', '2017-04-10 07:16:07.594368', '2017-04-10 07:16:07.594368', '2', '5', '数据挖掘', '30');
INSERT INTO `forum_subclass` VALUES ('8', 'computer-networking', '2017-04-10 07:16:43.359887', '2017-04-10 07:16:43.359887', '2', '5', '计算机网络', '30');
INSERT INTO `forum_subclass` VALUES ('9', 'go', '2017-04-11 01:12:52.471429', '2017-04-11 01:12:52.471429', '2', '2', 'GO', '13');
INSERT INTO `forum_subclass` VALUES ('10', 'job-hopping', '2017-04-11 07:14:57.157715', '2017-04-11 07:14:57.157715', '2', '12', '跳槽', '10');
INSERT INTO `forum_subclass` VALUES ('11', 'colleague', '2017-04-11 07:15:42.264294', '2017-04-11 07:15:42.264294', '2', '12', '同事', '50');
INSERT INTO `forum_subclass` VALUES ('12', 'change-profession', '2017-04-11 07:16:15.405058', '2017-04-11 07:16:15.405058', '2', '12', '转行', '60');
INSERT INTO `forum_subclass` VALUES ('13', 'c-plus-plus', '2017-04-11 07:16:48.754104', '2017-04-11 07:16:48.754104', '2', '2', 'C++', '100');
INSERT INTO `forum_subclass` VALUES ('14', 'shenzhen', '2017-04-11 07:17:44.903232', '2017-04-11 07:17:44.903232', '2', '3', '深圳', '1');
INSERT INTO `forum_subclass` VALUES ('15', 'beijing', '2017-04-11 07:18:07.394083', '2017-04-11 07:18:07.394584', '2', '3', '北京', '1');
INSERT INTO `forum_subclass` VALUES ('16', 'guangzhou', '2017-04-11 07:18:20.305297', '2017-04-11 07:18:20.305297', '2', '3', '广州', '1');
INSERT INTO `forum_subclass` VALUES ('17', 'shanghai', '2017-04-11 07:18:32.863794', '2017-04-11 07:18:32.863794', '2', '3', '上海', '1');
INSERT INTO `forum_subclass` VALUES ('18', 'hangzhou', '2017-04-11 07:18:49.648593', '2017-04-11 07:18:49.648593', '2', '3', '杭州', '1');
INSERT INTO `forum_subclass` VALUES ('19', 'renting', '2017-04-11 07:19:39.370902', '2017-04-11 07:19:39.370902', '2', '10', '租房', '1');
INSERT INTO `forum_subclass` VALUES ('20', 'outing', '2017-04-11 07:20:11.599195', '2017-04-11 07:20:11.599195', '2', '10', '出行', '1');
INSERT INTO `forum_subclass` VALUES ('21', 'dress-up', '2017-04-11 07:21:31.963959', '2017-04-11 07:21:31.963959', '2', '10', '打扮', '1');
INSERT INTO `forum_subclass` VALUES ('22', 'make-friends', '2017-04-11 07:45:19.700290', '2017-04-11 07:45:19.700290', '2', '10', '交友', '1');
INSERT INTO `forum_subclass` VALUES ('23', 'programmer', '2017-04-11 07:46:31.653733', '2017-04-11 07:46:31.653733', '2', '5', '程序员', '1');

-- ----------------------------
-- Table structure for forum_tag
-- ----------------------------
DROP TABLE IF EXISTS `forum_tag`;
CREATE TABLE `forum_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of forum_tag
-- ----------------------------

-- ----------------------------
-- Table structure for forum_thread
-- ----------------------------
DROP TABLE IF EXISTS `forum_thread`;
CREATE TABLE `forum_thread` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tittle` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `last_time` datetime(6) DEFAULT NULL,
  `create_user_id` int(11) NOT NULL,
  `sub_class_id` int(11),
  `main_class_id` int(11),
  PRIMARY KEY (`id`),
  KEY `forum_thread_create_user_id_be494053_fk_auth_user_id` (`create_user_id`),
  KEY `forum_thread_main_class_id_2d48ffb7_fk_forum_class_id` (`main_class_id`),
  KEY `forum_thread_sub_class_id_d74dbc71_fk_forum_subclass_id` (`sub_class_id`),
  CONSTRAINT `forum_thread_create_user_id_be494053_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `forum_thread_main_class_id_2d48ffb7_fk_forum_class_id` FOREIGN KEY (`main_class_id`) REFERENCES `forum_class` (`id`),
  CONSTRAINT `forum_thread_sub_class_id_d74dbc71_fk_forum_subclass_id` FOREIGN KEY (`sub_class_id`) REFERENCES `forum_subclass` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of forum_thread
-- ----------------------------
INSERT INTO `forum_thread` VALUES ('1', '请问这个是什么', 'Hello JavaScriptss', '2017-04-11 10:39:13.019080', '2017-04-09 01:54:40.541265', '5', '1', '2');
INSERT INTO `forum_thread` VALUES ('2', '程序员的第一个贴子', '你好，世界s~ssssssss', '2017-04-11 10:58:23.694438', '2017-04-11 10:33:05.523561', '2', '23', null);
INSERT INTO `forum_thread` VALUES ('3', '程序员的第二个贴子', '测试一下吧s', '2017-04-11 11:34:03.368912', '2017-04-11 11:00:33.196109', '2', '23', '5');
INSERT INTO `forum_thread` VALUES ('4', '程序员的第三个贴子', '你还好吗?sssssssss', '2017-04-11 11:33:54.369391', '2017-04-11 11:03:45.413046', '4', '23', '5');
INSERT INTO `forum_thread` VALUES ('5', '你好,世界', '来自程序员的关怀', '2017-04-11 12:53:27.457895', '2017-04-11 12:53:27.457895', '4', '23', '5');
INSERT INTO `forum_thread` VALUES ('6', '如果硬盘被拆开如果被盗，会看到群晖里储存的东西吗', 'rt', '2017-04-11 12:59:51.418487', '2017-04-11 12:58:46.570729', '2', '23', '5');
INSERT INTO `forum_thread` VALUES ('7', '这是云计算的第一个贴子', '云计算啦，开心的云计算', '2017-04-11 13:02:12.093460', '2017-04-11 13:02:12.093460', '11', '4', '5');
INSERT INTO `forum_thread` VALUES ('8', '中国人工智能产业数据图谱：55家医疗人工智能企业全扫描', '随着计算和存储的成本大幅下降，计算能力的显著增长，以及IT巨头所搭建的人工智能生态逐渐完善，人工智能初创企业的难度在降低。可喜的是，近两年人工智能也深受资本的青睐，2017年第一季度就有30多家人工智能企业获得融资，落实到具体行业中，医疗健康领域的人工智能创业公司表现尤为突出，关注度和融资量最高。\r\n　　在虚拟助理、医疗大数据、医学影像、等医学领域，人工智能已经不再仅仅是探讨、研究了，大多数产品已经在服务我们普通大众。对此，动脉网对中国的医疗人工智能企业进行了盘点，了解一下中国医疗人工智能企业的发展现状。\r\n　　此次，动脉网收集的医疗人工智能企业合计55家，共分为9个领域：虚拟助理、医疗大数据、医学影像、智能语音、健身生物技术、健康生活方式管理、医疗搜索、癌症早筛、人工智能芯片。\r\n　　其中，上市公司有5家，获得融资的有24家，不包含上市公司，医疗人工智能创业企业共融资22.355亿人民币（数千万、数百万按照1000万、100万计算），未透露的有26家，参与医疗人工智能投资的机构和企业一共有59家（由于时间和信息量的关系，相信我们收集的数据并不全面，未收录到的企业和机构请与我们联系）。', '2017-04-11 16:02:13.194125', '2017-04-11 16:02:13.194629', '2', '5', '5');

-- ----------------------------
-- Table structure for forum_usersummer
-- ----------------------------
DROP TABLE IF EXISTS `forum_usersummer`;
CREATE TABLE `forum_usersummer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of forum_usersummer
-- ----------------------------

-- ----------------------------
-- Table structure for index_userprofile
-- ----------------------------
DROP TABLE IF EXISTS `index_userprofile`;
CREATE TABLE `index_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language` varchar(10) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `work_place` varchar(20) NOT NULL,
  `work_nickname` varchar(20) NOT NULL,
  `self_introduction` varchar(300) NOT NULL,
  `set_avatar` tinyint(1) NOT NULL,
  `work_year` int(11) NOT NULL,
  `blog_adderss` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`) USING BTREE,
  CONSTRAINT `index_userprofile_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of index_userprofile
-- ----------------------------
INSERT INTO `index_userprofile` VALUES ('1', null, '1', '', '', '', '', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('2', 'EN-ju', '2', 'ava/2_4ydFf85.jpg', '华为大工厂s', '产品经理s', '明天天气晴朗', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('3', null, '3', '', '', '', '', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('4', null, '4', '', '', '', '', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('5', null, '5', '', '', '', '', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('6', null, '6', '', '', '', '', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('7', 'ch', '7', 'ava/7.jpg', '腾讯TSG', '老板', '一个菜鸟', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('8', null, '8', '', '', '', '', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('9', 'dd', '9', 'ava/9.jpg', 'dd', 'dd', 'dd', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('10', null, '10', '/default-user-image.png', '', '', '', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('11', 'ss', '11', 'ava/11_2QT5W6D.jpg', 's', 's', 'sssss', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('12', 'dfjhkh', '12', 'ava/12.jpg', 'jhsdifh', 'dshfi', 'dfhisod', '0', '0', '');
INSERT INTO `index_userprofile` VALUES ('13', null, '13', '/default-user-image.png', '', '', '', '0', '0', '');

-- ----------------------------
-- Table structure for lab_addmodel
-- ----------------------------
DROP TABLE IF EXISTS `lab_addmodel`;
CREATE TABLE `lab_addmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `a1` int(11) NOT NULL,
  `a2` int(11) NOT NULL,
  `result` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lab_addmodel
-- ----------------------------

-- ----------------------------
-- Table structure for lab_postmodel
-- ----------------------------
DROP TABLE IF EXISTS `lab_postmodel`;
CREATE TABLE `lab_postmodel` (
  `time` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tittle` varchar(30) NOT NULL,
  `content` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_postmodel_user_id_661491db_fk_auth_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `lab_postmodel_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lab_postmodel
-- ----------------------------

-- ----------------------------
-- Table structure for message_eventmessage
-- ----------------------------
DROP TABLE IF EXISTS `message_eventmessage`;
CREATE TABLE `message_eventmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message_eventmessage
-- ----------------------------

-- ----------------------------
-- Table structure for message_systemtousermessage
-- ----------------------------
DROP TABLE IF EXISTS `message_systemtousermessage`;
CREATE TABLE `message_systemtousermessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(500),
  `read` tinyint(1) NOT NULL,
  `time` time(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `message_systemtousermessage_user_id_a1bb9692_fk_auth_user_id` (`user_id`),
  CONSTRAINT `message_systemtousermessage_user_id_a1bb9692_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message_systemtousermessage
-- ----------------------------
INSERT INTO `message_systemtousermessage` VALUES ('1', 'welcome,you hehe', '0', '13:34:36.227593', '2');

-- ----------------------------
-- Table structure for message_usertousermessage
-- ----------------------------
DROP TABLE IF EXISTS `message_usertousermessage`;
CREATE TABLE `message_usertousermessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message_usertousermessage
-- ----------------------------

-- ----------------------------
-- Table structure for setting_systememailinfo
-- ----------------------------
DROP TABLE IF EXISTS `setting_systememailinfo`;
CREATE TABLE `setting_systememailinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email_address` varchar(255) NOT NULL,
  `name` varchar(20) NOT NULL,
  `port` int(11) NOT NULL,
  `protocal` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of setting_systememailinfo
-- ----------------------------

-- ----------------------------
-- Table structure for timeline_comment
-- ----------------------------
DROP TABLE IF EXISTS `timeline_comment`;
CREATE TABLE `timeline_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(600) NOT NULL,
  `created_time` datetime NOT NULL,
  `last_operate` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `timeline_comment_user_id_971300bb_fk_auth_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `timeline_comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of timeline_comment
-- ----------------------------
INSERT INTO `timeline_comment` VALUES ('1', '你好世界', '2017-04-07 07:24:35', '2017-04-07 07:24:35', '2');
INSERT INTO `timeline_comment` VALUES ('2', '我都不知道你在说什么', '2017-04-07 07:29:38', '2017-04-07 07:29:38', '9');
INSERT INTO `timeline_comment` VALUES ('3', '我今天吃了', '2017-04-09 07:04:40', '2017-04-09 07:04:40', '7');
INSERT INTO `timeline_comment` VALUES ('4', 'sss', '2017-04-09 08:13:51', '2017-04-09 08:13:51', '2');
INSERT INTO `timeline_comment` VALUES ('5', 'Hello world?', '2017-04-09 08:14:01', '2017-04-09 08:14:01', '2');
INSERT INTO `timeline_comment` VALUES ('6', '<script></script>', '2017-04-09 08:14:37', '2017-04-09 08:14:37', '2');
INSERT INTO `timeline_comment` VALUES ('7', '你看一下离你最近的节点是哪里，日本的线路现在已经大不如前了，如果你一定要买日本的，那就选 IIJ 线路的。香港那边的话，如果你经常看 TVB 也是不错的选择，但是好线路也通常需要很大的投入，那么剩下的选择也不多了，比如泡菜国或者俄罗斯。说到这里，你应该知道了要找哪里的 VPS 了。剩下的的无非就是 vps 的优化，太冗长了。如果你有兴趣的话，发邮件给我吧。:)', '2017-04-09 08:17:27', '2017-04-09 08:17:27', '12');
INSERT INTO `timeline_comment` VALUES ('8', 'GigsGigsCloud 这是啥玩意啊，看到这么便宜，寻思买一个玩玩，结果就是主机加载不出来。开工单没人回复，垃圾的节奏，浪费了$3.8...', '2017-04-09 08:53:49', '2017-04-09 08:53:49', '2');
INSERT INTO `timeline_comment` VALUES ('9', 'GigsGigsCloud 这是啥玩意啊，看到这么便宜，寻思买一个玩玩，结果就是主机加载不出来。开工单没人回复，垃圾的节奏，浪费了$3.8...', '2017-04-09 08:55:09', '2017-04-09 08:55:09', '2');
INSERT INTO `timeline_comment` VALUES ('35', 'hello woreld?', '2017-04-09 12:49:59', '2017-04-09 12:49:59', '2');
INSERT INTO `timeline_comment` VALUES ('36', 'hello woreld?', '2017-04-09 12:50:17', '2017-04-09 12:50:17', '2');
INSERT INTO `timeline_comment` VALUES ('37', 'hello world?asas', '2017-04-09 14:41:40', '2017-04-09 14:41:40', '2');
INSERT INTO `timeline_comment` VALUES ('38', 'RT,手机是 Nexus 6,系统是魔趣的 60.1(android 6.0.1)。\r\n现在屏幕包括内屏全都坏了，除了几个亮点漆黑一片。但是其它部件应该没问题，因为刚坏那几天早上它的闹钟还按时响呢。\r\n电脑上有驱动，但是连上不去默认是充电模式(设置里面设置默认改了的，但是以前每次用都还要手动去选 MTP 的 USB 打开方式，不知道是不是 BUG)\r\n本来准备丢那不要了，最近要写一篇报告，才发现几张重要照片还在里面并且还没来得及同步到 google photos 。 有啥办法能从手机里面把照片弄出来吗？\r\n实在不想去换屏，内屏都坏了，修的价格还不如买新的......', '2017-04-09 14:42:07', '2017-04-09 14:42:07', '12');
INSERT INTO `timeline_comment` VALUES ('39', 'https://wj.qq.com/s/1206919/4d9d\r\n如果你或你身边的有朋友(仅限学生)想学习前端开发(网页开发、网站建设、 JavaScript 等技术)，我们正在免费招募一些学习者。\r\n学习方式：线上交流，每天会有规定的任务，以及专门的指导，有兴趣，有时间，而且能够长期坚持的朋友快来报名吧。\r\n这一期报名截止时间：2017 年 4 月 17 日\r\n转发给身边有需要的学生朋友~~', '2017-04-10 00:28:32', '2017-04-10 00:28:32', '2');
INSERT INTO `timeline_comment` VALUES ('40', '难受想哭', '2017-04-10 03:19:33', '2017-04-10 03:19:33', '2');
INSERT INTO `timeline_comment` VALUES ('41', '世界信息互通联盟_百度搜索 https://www.baidu.com/s?ie=UTF-8&wd=%E4%B8%96%E7%95%8C%E4%BF%A1%E6%81%AF%E4%BA%92%E9%80%9A%E8%81%94%E7%9B%9F', '2017-04-10 12:48:37', '2017-04-10 12:48:37', '2');
INSERT INTO `timeline_comment` VALUES ('42', 'https://wj.qq.com/s/1206919/4d9d\r\n如果你或你身边的有朋友(仅限学生)想学习前端开发(网页开发、网站建设、 JavaScript 等技术)，我们正在免费招募一些学习者。\r\n学习方式：线上交流，每天会有规定的任务，以及专门的指导，有兴趣，有时间，而且能够长期坚持的朋友快来报名吧。\r\n这一期报名截止时间：2017 年 4 月 17 日\r\n转发给身边有需要的学生朋友~~', '2017-04-10 12:49:06', '2017-04-10 12:49:06', '2');
INSERT INTO `timeline_comment` VALUES ('43', 'Hello', '2017-04-10 14:34:45', '2017-04-10 14:34:45', '2');
INSERT INTO `timeline_comment` VALUES ('44', '我都不知道我在做什么', '2017-04-10 15:19:33', '2017-04-10 15:19:33', '2');
INSERT INTO `timeline_comment` VALUES ('45', '早上好，今天又是美好的一天', '2017-04-11 00:14:50', '2017-04-11 00:14:50', '2');
INSERT INTO `timeline_comment` VALUES ('46', '1、本套试卷来源于网上，由牛客网注册用户提供，除非经特别声明，牛客网不拥有该资料版权，亦不承担任何法律责任。\r\n2、未经网站或作者的同意不得转载，否则构成侵权，本网站或作者保留诉诸法律的权利。\r\n3、如发现本网站载有侵犯您著作权的侵权信息，可依法向我们提出权利申请，申请方式点击查看。', '2017-04-11 01:10:08', '2017-04-11 01:10:08', '7');
INSERT INTO `timeline_comment` VALUES ('47', 'sss', '2017-04-11 03:47:00', '2017-04-11 03:47:00', '2');
INSERT INTO `timeline_comment` VALUES ('48', '...我很忧郁', '2017-04-11 12:47:07', '2017-04-11 12:47:07', '2');
INSERT INTO `timeline_comment` VALUES ('49', '我也来试试提交表单', '2017-04-11 14:23:58', '2017-04-11 14:23:58', '13');
INSERT INTO `timeline_comment` VALUES ('50', '我也来试试提交表单', '2017-04-11 14:24:36', '2017-04-11 14:24:36', '13');
INSERT INTO `timeline_comment` VALUES ('51', '我也来试试提交表单', '2017-04-11 14:24:40', '2017-04-11 14:24:40', '13');
INSERT INTO `timeline_comment` VALUES ('52', '看来看去，就“支付宝”那个 ICON 好看点。但是支付宝里面东西太多，集天猫，淘宝，支付宝，美团， 58 ，朋友圈，等等。所以老早卸载不用了，现在主要使用微信付款转账等。\r\n\r\n主要说是 ICON ， LOGO （游戏类的除外）。看那些 LOGO 一个都不想下，这么美的 iphone ，那么丑的 ICON ，简直恶心到爆。\r\n\r\n使用 iphone ，只有下载国外的 ICON ，那个界面看起来才一致。\r\n\r\n我比较审美洁癖，请清拍！\r\n\r\n现在我的 APP 只有：招商银行(丑丑丑)， slack ， twitter ，微信(及格)，有邻(这个不错)，网易云音乐(太丑了)， ofo(褪不去的山寨范).', '2017-04-11 14:35:11', '2017-04-11 14:35:11', '2');
INSERT INTO `timeline_comment` VALUES ('53', '要好好加油了啊↖(^ω^)↗', '2017-04-11 15:34:43', '2017-04-11 15:34:43', '2');
