-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 11, 2019 at 01:23 AM
-- Server version: 5.7.25-0ubuntu0.16.04.2
-- PHP Version: 7.0.33-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `product_name` text NOT NULL,
  `product_size` text,
  `product_price` int(11) NOT NULL,
  `product_qty` int(10) NOT NULL,
  `product_image` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `product_size`, `product_price`, `product_qty`, `product_image`) VALUES
(1, 'blue sherpa trucker', 'S,M,L', 300, 100, '/static/1trucker'),
(2, 'black sherpa trucker', 'S,M,L', 300, 100, '2trucker.jpg'),
(3, 'original trucker', '', 400, 100, '3trucker'),
(4, ' trucker jeans', '', 500, 100, '0'),
(5, 'skinny jeans', '', 350, 100, '0'),
(6, 'slim jeans', '', 400, 100, '0'),
(7, 'athletic jeans', '', 400, 100, '0'),
(8, 'straight jeans', '', 450, 100, '0'),
(9, 'relaxed jeans', '', 350, 100, '0'),
(15, 'leather jacket', '', 600, 30, '0'),
(19, 'sherpa trucker', 'S,M,L', 300, 100, '0'),
(20, 'sherpa trucker', 'S', 100, 100, '0'),
(21, 'bkas', 's', 300, 300, '0');

-- --------------------------------------------------------

--
-- Table structure for table `shoppingcart`
--

CREATE TABLE `shoppingcart` (
  `shoppingcart_user_name` varchar(20) NOT NULL,
  `s_product_name` text NOT NULL,
  `product_size` text NOT NULL,
  `product_quantity` varchar(20) NOT NULL,
  `product_price` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `uorder`
--

CREATE TABLE `uorder` (
  `order_user_name` varchar(20) NOT NULL,
  `orderproducts` text NOT NULL,
  `orderproductQTY` int(20) NOT NULL,
  `order_product_size` text NOT NULL,
  `product_price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `uorder`
--

INSERT INTO `uorder` (`order_user_name`, `orderproducts`, `orderproductQTY`, `order_product_size`, `product_price`) VALUES
('jimmy', 'blue sherpa trucker', 3, 's', 300),
('jimmy', 'black sherpa trucker', 3, 's', 300),
('asdads', 'blue sherpa trucker', 3, 'S', 300),
('sasda12', 'blue sherpa trucker', 3, 's', 300),
('qrt', 'blue sherpa trucker', 3, 's', 300);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `Name` varchar(10) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `Name`, `Email`, `Phone`) VALUES
(1, 'admin', 'admin', NULL, NULL, NULL),
(2, 'jimmy', '1211', 'Yipka', 'jimmy@gmail.com', 1211211),
(3, 'abc', '123', 'asd', '', 8),
(4, 'aaa', '123', NULL, NULL, NULL),
(5, 'asdad', '123', NULL, NULL, NULL),
(6, 'aaa121', '121', NULL, NULL, NULL),
(7, 'hjk123', '123', NULL, NULL, NULL),
(8, 'asdas12', '123', NULL, NULL, NULL),
(9, 'jkl123', '123', NULL, NULL, NULL),
(10, 'a123123', '1231', NULL, NULL, NULL),
(11, 'asdads', '123', 'Yipka', 'jimmy@gmail.com', 121212),
(12, 'sasda12', '123', 'Yipka', 'jimmy@gmail.com', 121212),
(13, 'qrt', '123', 'Yipka', 'jimmy@gmail.com', 12212);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`),
  ADD UNIQUE KEY `product_id` (`product_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
