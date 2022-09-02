create database CO2;
SET GLOBAL local_infile=1;
USE CO2;

drop table if exists pais;
create table pais(
	idx int,
    codigo_iso VARCHAR(30),
    pais VARCHAR(30)
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tabla_pais.csv"
into table pais
fields terminated by ","
lines terminated by '\r'
ignore 1 lines;


drop table if exists central_electrica;
create table central_electrica(
	idx int,
    codigo_iso VARCHAR(30),
    pais VARCHAR(30),
    nombre VARCHAR(100),
    capacidad_MW decimal(12,2),
    latitud decimal(12,2),
    longitud decimal(12,2),
    energia_primaria VARCHAR(30),
    otra_energia1 VARCHAR(30),
    anio_apertura int,
    anio_capacidad_reportada decimal(12,2),
    anio int,
    gwh_x_anio decimal(12,2)
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/NORMALIZADO_central_electrica.csv"
into table central_electrica
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;


drop table if exists energyco2;
create table energyco2(
	idx int,
    pais VARCHAR(30), 
    tipo_energia VARCHAR(30),
    anio int,
    Energy_consumption decimal(12,2),
    Energy_production decimal(12,2),
    PBI decimal(12,2),
    Population decimal(12,2),
    Energy_production_per_capita decimal(12,2),
    Energy_intensity_by_GDP decimal(12,2),
    CO2_emission decimal(12,2)
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/energyco2_normalizado.csv"
into table energyco2
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;

drop table if exists climate_disasters;
create table climate_disasters(
    pais VARCHAR(30),
    codigo_iso text,
    indicador VARCHAR(30), 
    anio int,
    frecuencia int
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/desastres_naturales/Climate-related_Disasters_Frequency_normalizado.csv"
into table climate_disasters
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;
SELECT * FROM climate_disasters;



drop table if exists M_E_S;
create table M_E_S(
    idx int,
    anio int,
    mes int,
    pais VARCHAR(30),
    balance VARCHAR(30), 
    producto VARCHAR(30), 
    cons_energia_gwh decimal(12,2)
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/energia_estadistica_mensual/MES_O522_normalizado.csv"
into table M_E_S
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;

drop table if exists acceso_electricidad;
create table acceso_electricidad(
    idx int,
    pais VARCHAR(30),
    codigo_iso VARCHAR(30),
    anio int,
    porcentaje float,
    info_codigo float
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/energias_renovables/NORMALIZADO_acceso_a_electricidad.csv"
into table acceso_electricidad
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;


drop table if exists intensidad_electricidad;
create table intensidad_electricidad(
    idx int,
    pais VARCHAR(30),
    codigo_iso VARCHAR(30),
    anio int,
    valor decimal(12,2),
    info_codigo decimal(12,2)
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/energias_renovables/NORMALIZADO_intensidad_electricidad_primaria.csv"
into table intensidad_electricidad
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;


drop table if exists data_ER;
create table data_ER(
    idx int,
    pais VARCHAR(30),
    codigo_iso VARCHAR(30),
    anio int,
    valor decimal(12,2),
    info_codigo decimal(12,2)
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/energias_renovables/NORMALIZADO_data_energia_renovable.csv"
into table data_ER
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;


drop table if exists energy_consumption;
create table energy_consumption(
    idx int,
    pais VARCHAR(30),
    anio int,
    codigo_iso VARCHAR(30),
    poblacion float(12,1),
    PBI float(12,1),
    biocombustible_cons decimal(12,2),
    biocombustible_elec decimal(12,2),
    biocombustible_share_energia decimal(12,2),
    carbon_intensidad_elec decimal(12,2),
    carbon_cons decimal(12,2),
    carbon_elec decimal(12,2),
    carbon_produccion decimal(12,2),
    elec_demand decimal(12,2),
    elec_generation decimal(12,2),
    energia_per_pbi decimal(12,2),
    fossil_elec decimal(12,2),
    fossil_combustible_cons decimal(12,2),
    gas_cons decimal(12,2),
    gas_elec decimal(12,2),
    gas_produccion decimal(12,2),
    greenhouse_gas_emision_co2s decimal(12,2),
    hydro_cons decimal(12,2),
    hydro_elec decimal(12,2),
    low_carbon_cons decimal(12,2),
    low_carbon_elec decimal(12,2),
    net_elec_imports decimal(12,2),
    nuclear_cons decimal(12,2),
    nuclear_elec decimal(12,2),
    petroleo_cons decimal(12,2),
    petroleo_elec decimal(12,2),
    petroleo_produccion decimal(12,2),
    other_renovable_cons decimal(12,2),
    other_renovable_elec decimal(12,2),
    other_renewable_exc_biocombustible_elec decimal(12,2),
    primary_energia_cons decimal(12,2),
    renovables_cons decimal(12,2),
    renovables_elec decimal(12,2),
    solar_cons decimal(12,2),
    solar_elec decimal(12,2),
    eolica_cons decimal(12,2),
    eolica_elec decimal(12,2),
    eolica_share_energia decimal(12,2)
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/energy_consumption/owid-energy-consumption-source_normalizado.csv"
into table energy_consumption
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;


drop table if exists cancer_pulmon;
create table cancer_pulmon(
    idx int,
    pais VARCHAR(30),
    anio int,
    casos_F int,
    casos_M int
);
LOAD DATA local INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/enfermedades/casos_cancer_pulmon_fym_NORMALIZADO.csv"
into table cancer_pulmon
fields terminated by ";"
lines terminated by '\r'
ignore 1 lines;