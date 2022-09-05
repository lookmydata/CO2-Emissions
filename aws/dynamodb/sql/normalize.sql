USE co2;

SET GLOBAL log_bin_trust_function_creators = 1;
DROP FUNCTION IF EXISTS `UC_Words`;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `UC_Words`( str VARCHAR(255) ) RETURNS varchar(255) CHARSET utf8
BEGIN  
  DECLARE c CHAR(1);  
  DECLARE s VARCHAR(255);  
  DECLARE i INT DEFAULT 1;  
  DECLARE bool INT DEFAULT 1;  
  DECLARE punct CHAR(17) DEFAULT ' ()[]{},.-_!@;:?/';  
  SET s = LCASE( str );  
  WHILE i < LENGTH( str ) DO  
     BEGIN  
       SET c = SUBSTRING( s, i, 1 );  
       IF LOCATE( c, punct ) > 0 THEN  
        SET bool = 1;  
      ELSEIF bool=1 THEN  
        BEGIN  
          IF c >= 'a' AND c <= 'z' THEN  
             BEGIN  
               SET s = CONCAT(LEFT(s,i-1),UCASE(c),SUBSTRING(s,i+1));  
               SET bool = 0;  
             END;  
           ELSEIF c >= '0' AND c <= '9' THEN  
            SET bool = 0;  
          END IF;  
        END;  
      END IF;  
      SET i = i+1;  
    END;  
  END WHILE;  
  RETURN s;  
END$$
DELIMITER ;

ALTER TABLE acceso_electricidad DROP COLUMN idx;
ALTER TABLE cancer_pulmon DROP COLUMN idx;
ALTER TABLE central_electrica DROP COLUMN idx;
ALTER TABLE m_e_s DROP COLUMN idx;
ALTER TABLE intensidad_electricidad DROP COLUMN idx;
ALTER TABLE energyco2 DROP COLUMN idx;
ALTER TABLE energy_consumption DROP COLUMN idx;
ALTER TABLE data_er DROP COLUMN idx;
ALTER TABLE pais DROP COLUMN idx;


		-- DROP NULL ROW --
DELETE FROM acceso_electricidad WHERE pais IS NULL;
DELETE FROM cancer_pulmon WHERE pais IS NULL;
DELETE FROM central_electrica WHERE pais IS NULL;
DELETE FROM m_e_s WHERE pais IS NULL;
DELETE FROM intensidad_electricidad WHERE pais IS NULL;
DELETE FROM energyco2 WHERE pais IS NULL;
DELETE FROM energy_consumption WHERE pais IS NULL;
DELETE FROM data_er WHERE pais IS NULL;
DELETE FROM climate_disasters WHERE codigo_iso IS NULL;
DELETE FROM pais WHERE codigo_iso IS NULL;


		-- NORMALIZACION --
ALTER TABLE acceso_electricidad change `codigo_iso` `codigo_iso2` VARCHAR(30);
ALTER TABLE acceso_electricidad add `codigo_iso` VARCHAR(30) first;
UPDATE acceso_electricidad set codigo_iso=codigo_iso2;
ALTER TABLE acceso_electricidad DROP COLUMN codigo_iso2;
SELECT * FROM acceso_electricidad;


ALTER TABLE central_electrica 
	CHANGE `codigo_iso` `codigo_iso2` VARCHAR(30),
	CHANGE anio anio2 INT,
    CHANGE anio_apertura anio_apertura2 INT;
ALTER TABLE central_electrica 
	ADD `codigo_iso` VARCHAR(30) first,
	ADD anio INT AFTER pais,
    ADD anio_apertura INT AFTER anio;
UPDATE central_electrica 
	SET codigo_iso=codigo_iso2,
		anio=anio2,
		anio_apertura=anio_apertura2;
ALTER TABLE central_electrica 
	DROP COLUMN anio_apertura2,
    DROP COLUMN anio2,
    DROP COLUMN codigo_iso2,
    DROP COLUMN anio_capacidad_reportada;
SELECT * FROM central_electrica;


ALTER TABLE intensidad_electricidad change `codigo_iso` `codigo_iso2` VARCHAR(30);
ALTER TABLE intensidad_electricidad add `codigo_iso` VARCHAR(30) first;
UPDATE intensidad_electricidad set codigo_iso=codigo_iso2;
ALTER TABLE intensidad_electricidad DROP COLUMN codigo_iso2;


ALTER TABLE energy_consumption change `codigo_iso` `codigo_iso2` VARCHAR(30);
ALTER TABLE energy_consumption add `codigo_iso` VARCHAR(30) first;
UPDATE energy_consumption set codigo_iso=codigo_iso2;
ALTER TABLE energy_consumption DROP COLUMN codigo_iso2;
SELECT * FROM energy_consumption;

ALTER TABLE data_er change `codigo_iso` `codigo_iso2` VARCHAR(30);
ALTER TABLE data_er add `codigo_iso` VARCHAR(30) first;
UPDATE data_er set codigo_iso=codigo_iso2;
ALTER TABLE data_er DROP COLUMN codigo_iso2;


ALTER TABLE climate_disasters
	CHANGE `codigo_iso` `codigo_iso2` VARCHAR(30),
    CHANGE anio anio2 INT;
ALTER TABLE climate_disasters
	ADD codigo_iso VARCHAR(30) FIRST,
    ADD anio INT AFTER pais;
UPDATE climate_disasters
	SET codigo_iso=codigo_iso2,
		anio=anio2;
ALTER TABLE climate_disasters
	DROP COLUMN codigo_iso2,
    DROP COLUMN anio2;

ALTER TABLE energyco2
	CHANGE `anio` `anio2` VARCHAR(30);
ALTER TABLE energyco2
	ADD anio INT AFTER pais;
UPDATE energyco2
	SET	anio=anio2;
ALTER TABLE energyco2
    DROP COLUMN anio2;

ALTER TABLE m_e_s
	CHANGE `pais` `pais2` VARCHAR(30);
ALTER TABLE m_e_s
	ADD pais VARCHAR(30) FIRST;
UPDATE m_e_s
	SET	pais=pais2;
ALTER TABLE m_e_s
	DROP COLUMN pais2;


		-- MAYUSCULAS --
UPDATE acceso_electricidad SET pais= UC_Words(TRIM(pais));
UPDATE cancer_pulmon SET pais= UC_Words(TRIM(pais));
UPDATE central_electrica SET pais= UC_Words(TRIM(pais)),
						nombre= UC_Words(TRIM(nombre));
UPDATE m_e_s SET pais= UC_Words(TRIM(pais)),
				balance= UC_Words(TRIM(balance)),
                producto=UC_Words(TRIM(producto));
UPDATE intensidad_electricidad SET pais= UC_Words(TRIM(pais));
UPDATE energyco2 SET pais= UC_Words(TRIM(pais)),
		tipo_energia=UC_Words(TRIM(tipo_energia));
UPDATE data_er SET pais= UC_Words(TRIM(pais));
UPDATE energy_consumption SET pais= UC_Words(TRIM(pais));
UPDATE climate_disasters SET pais= UC_Words(TRIM(pais)),
					indicador= UC_Words(TRIM(indicador));