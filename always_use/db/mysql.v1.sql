-- 默认库是matrix库，没有的需手动创建

-- ----------------------------------
-- !! 删除表操作，操作前请注意备份数据 !! --
-- ----------------------------------
DROP TABLE IF EXISTS `app_base_info`;
CREATE TABLE IF NOT EXISTS `app_base_info`
(
    `id`               int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增主键',
    `app_name`         varchar(50)  NOT NULL COMMENT '应用名称',
    `app_version`      varchar(50)  NOT NULL COMMENT '应用版本',
    `app_size`         float        NOT NULL COMMENT 'app大小',
    `minSdkVersion`    int unsigned DEFAULT 0 COMMENT '安装最低要求的SDK版本',
    `targetSdkVersion` int unsigned DEFAULT 0 COMMENT '目标要求的SDK版本',
    `create_time`      timestamp    DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time`      timestamp    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
    `deleted`          bool         DEFAULT 0 COMMENT '默认0，表示未被删除，1表示被软删除',
    `comment`          varchar(100) DEFAULT '' COMMENT '备注',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE utf8mb4_unicode_ci
  ROW_FORMAT = Dynamic
    COMMENT 'apk基础信息表';


insert into app_base_info(app_name, app_version, app_size, minSdkVersion, targetSdkVersion)
values ('com.xxx.qq', 'app_version', 100, 19, 26)


