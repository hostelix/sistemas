-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-08-2013 a las 02:03:49
-- Versión del servidor: 5.5.27
-- Versión de PHP: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `sistemas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_cedulas`
--

CREATE TABLE IF NOT EXISTS `pagina_cedulas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cedula_user` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula_user` (`cedula_user`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=28 ;

--
-- Volcado de datos para la tabla `pagina_cedulas`
--

INSERT INTO `pagina_cedulas` (`id`, `cedula_user`) VALUES
(12, 20679253),
(11, 21113870),
(25, 21114065),
(3, 21667358),
(26, 22508821),
(1, 22602571),
(19, 22602604),
(22, 22608516),
(7, 23588219),
(5, 23624283),
(14, 23673395),
(13, 23674721),
(20, 23678371),
(17, 24307017),
(6, 24308395),
(2, 24352432),
(16, 24352838),
(4, 24352847),
(9, 24562808),
(18, 24589591),
(8, 24622599),
(27, 24622920),
(23, 24674782),
(15, 24717174),
(10, 25096188),
(24, 25557188),
(21, 25613233);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
