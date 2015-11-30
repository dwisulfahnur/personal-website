-- phpMyAdmin SQL Dump
-- version 4.2.12deb2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 01, 2015 at 02:12 AM
-- Server version: 5.5.44-0+deb8u1
-- PHP Version: 5.6.13-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `personal_website`
--

-- --------------------------------------------------------

--
-- Table structure for table `activities`
--

CREATE TABLE IF NOT EXISTS `activities` (
`id` int(11) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `created` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `activities`
--

INSERT INTO `activities` (`id`, `title`, `content`, `created`) VALUES
(1, 'Personal Website', 'Ini adalah pertama kalinya saya membuat project menggunakan Framework berbasis Python yaitu Microframework Flask dari Python', '30/11/2015'),
(2, 'Dwi Sulfahnur', ' Perkenalkan nama saya adalah Dwi Sulfahnur, saya sedang melakukan studi di Politeknik negeri Ujung Pandang Jurusan Elektro Prodi Teknik Telekomunikasi', '30/11/2015');

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE IF NOT EXISTS `blog` (
`id` int(11) NOT NULL,
  `title` text NOT NULL,
  `author` text NOT NULL,
  `content` text NOT NULL,
  `created` text NOT NULL,
  `category` int(11) NOT NULL,
  `category_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blog`
--

INSERT INTO `blog` (`id`, `title`, `author`, `content`, `created`, `category`, `category_id`) VALUES
(6, 'facebook', 'Dwi Sulfahnur', 'Facebook adalah sosial media yang dibuat dengan php', '30/11/2015', 0, 2),
(7, 'Python', 'Dwi Sulfahnur', 'Python adalah', '30/11/2015', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE IF NOT EXISTS `category` (
`id` int(11) NOT NULL,
  `name_category` text NOT NULL,
  `created` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name_category`, `created`) VALUES
(1, 'PROGRAMMING', '30/11/2015'),
(2, 'SOSIAL MEDIA', '30/11/2015');

-- --------------------------------------------------------

--
-- Table structure for table `personal_information`
--

CREATE TABLE IF NOT EXISTS `personal_information` (
`id` int(11) NOT NULL,
  `full_name` text NOT NULL,
  `avatar` text NOT NULL,
  `job` text NOT NULL,
  `organization` text NOT NULL,
  `address` text NOT NULL,
  `github` text NOT NULL,
  `facebook` text NOT NULL,
  `twitter` text NOT NULL,
  `no_hp` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `personal_information`
--

INSERT INTO `personal_information` (`id`, `full_name`, `avatar`, `job`, `organization`, `address`, `github`, `facebook`, `twitter`, `no_hp`) VALUES
(1, 'Dwi Sulfahnur', 'img/ds.jpg', 'Student', 'PNUP', 'Makassar', 'https://github.com/dwisulfahnur', 'https://facebook.com/dwisulfahnur', 'https://twitter.com/dwi_sulfahnur', '+6282292300394');

-- --------------------------------------------------------

--
-- Table structure for table `photos`
--

CREATE TABLE IF NOT EXISTS `photos` (
`id` int(11) NOT NULL,
  `label` text NOT NULL,
  `url` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `photos`
--

INSERT INTO `photos` (`id`, `label`, `url`) VALUES
(1, 'HACKATHON', 'img/1.jpg'),
(3, '', 'img/2.jpg'),
(4, '', 'img/3.jpg'),
(5, '', 'img/4.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
`id` int(11) NOT NULL,
  `full_name` text NOT NULL,
  `email` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `full_name`, `email`, `username`, `password`) VALUES
(1, 'Dwi Sulfahur', 'dwisulfahnur@gmail.com', 'dwisulfahnur', 'pbkdf2:sha1:1000$hvfDGVgt$df93c0f49d96adda0a94ee2a6896fa858d3417fe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activities`
--
ALTER TABLE `activities`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `personal_information`
--
ALTER TABLE `personal_information`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `photos`
--
ALTER TABLE `photos`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activities`
--
ALTER TABLE `activities`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `personal_information`
--
ALTER TABLE `personal_information`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `photos`
--
ALTER TABLE `photos`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
