/* Create Table for Server */
CREATE TABLE `classes` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `name_of_class` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `type_of_course` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `lecturer` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `number` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `short_text` text COLLATE utf8_unicode_ci DEFAULT NULL,
 `choice_term` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `hours_per_week_in_term` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `expected_num_of_participants` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `maximum_participants` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `assignment` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `lecture_id` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `credit_points` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `hyperlink` text COLLATE utf8_unicode_ci DEFAULT NULL,
 `language` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `created_at` timestamp NULL DEFAULT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `events` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `class_id` int(10) unsigned NOT NULL,
 `start_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `end_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `day` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `start_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `end_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `frequency` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `room` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `lecturer_for_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `status` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `remarks` text COLLATE utf8_unicode_ci,
 `cancelled_on` text COLLATE utf8_unicode_ci,
 `max_participants` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `created_at` timestamp NULL DEFAULT NULL,
 PRIMARY KEY (`id`),
 KEY `events_class_id_foreign` (`class_id`),
 CONSTRAINT `events_class_id_cascade` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
