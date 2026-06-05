# Tuning Community

## Descripción General

Tuning Community es una aplicación web desarrollada con FastAPI para la gestión de proyectos de modificación automotriz.

El sistema permite registrar usuarios, vehículos base (Stock Cars), modificaciones (Mods) y Builds personalizadas, estableciendo relaciones entre todas las entidades mediante una API REST y una interfaz web desarrollada con Jinja2.

Además, incorpora almacenamiento de imágenes utilizando Supabase Storage y un Dashboard Analítico que permite visualizar estadísticas relevantes sobre los Builds registrados.

---

# Tecnologías Utilizadas

* FastAPI
* Pydantic v2
* Jinja2
* Bootstrap 5
* PostgreSQL
* Supabase
* Python 3.11+

---

# Organización de Carpetas

```text
app/
│
├── main.py
│
├── config/
│   └── settings.py
│
├── database/
│   └── supabase_client.py
│
├── enums/
│   ├── build_approach.py
│   ├── chassis_type.py
│   ├── fuel_type.py
│   └── mod_type.py
│
├── models/
│   ├── user.py
│   ├── stock_car.py
│   ├── build.py
│   ├── mod.py
│   └── build_mod.py
│
├── services/
│   ├── analytics_service.py
│   ├── build_mod_service.py
│   ├── build_service.py
│   ├── mod_service.py
│   ├── stock_car_service.py
│   ├── upload_service.py
│   ├── user_service.py
│   └── validator_service.py
│
├── routers/
│   │
│   ├── api/
│   │   ├── users.py
│   │   ├── stock_cars.py
│   │   ├── builds.py
│   │   ├── mods.py
│   │   └── build_mods.py
│   │
│   └── web/
│       ├── home.py
│       ├── dashboard.py
│       ├── users_web.py
│       ├── stock_cars_web.py
│       ├── builds_web.py
│       └── mods_web.py
│
├── templates/
│   │
│   ├── base.html
│   ├── home.html
│   ├── dashboard.html
│   │
│   ├── users/
│   │   ├── list.html
│   │   └── detail.html
│   │
│   ├── stock_cars/
│   │   ├── list.html
│   │   └── detail.html
│   │
│   ├── builds/
│   │   ├── list.html
│   │   └── detail.html
│   │
│   └── mods/
│       ├── list.html
│       └── detail.html
│
└── static/
    ├── css/
    ├── js/
    └── images/

```

---

# Arquitectura del Proyecto

La aplicación sigue una arquitectura por capas:

### Models

Contienen los esquemas Pydantic encargados de validar los datos de entrada y salida de la API.

### Services

Implementan toda la lógica de negocio y la comunicación con Supabase.

### API Routers

Exponen los endpoints REST utilizados por Swagger (/docs) y clientes externos.

### Web Routers

Renderizan las vistas HTML utilizando Jinja2.

### Templates

Contienen las páginas web del sistema.

### Database

Gestiona la conexión centralizada con Supabase.

### Enums

Definen valores controlados para campos específicos como:

- FuelType
- ChassisType
- BuildApproach
- ModType

### Analytics

Genera estadísticas para el Dashboard mediante consultas agregadas a la base de datos.

---

# Modelo Entidad Relación

## Users

Representa los usuarios registrados en la comunidad.

| Campo       | Tipo    |
| ----------- | ------- |
| id          | Integer |
| username    | String  |
| email       | String  |
| description | String  |
| picture     | URL     |

---

## Stock Cars

Representa vehículos base sobre los cuales pueden construirse proyectos de modificación.

| Campo            | Tipo        |
| ---------------- | ----------- |
| id               | Integer     |
| brand            | String      |
| model            | String      |
| production_start | Integer     |
| production_end   | Integer     |
| chassis_type     | ChassisType |
| fuel             | FuelType    |
| stock_hp         | Integer     |
| price            | Float       |
| picture          | URL         |

---

## Builds

Representa proyectos completos de modificación.

| Campo          | Tipo          |
| -------------- | ------------- |
| id             | Integer       |
| user_id        | Integer       |
| stock_car_id   | Integer       |
| build_name     | String        |
| build_approach | BuildApproach |
| engine         | String        |
| year           | Integer       |
| hp             | Integer       |
| price          | Float         |
| picture        | URL           |

---

## Mods

Representa componentes o modificaciones disponibles para instalar.

| Campo     | Tipo    |
| --------- | ------- |
| id        | Integer |
| type_mod  | ModType |
| brand     | String  |
| reference | String  |
| name      | String  |
| price     | Float   |
| picture   | URL     |

---

## Build Mods

Tabla puente para la relación muchos a muchos entre Builds y Mods.

| Campo    | Tipo    |
| -------- | ------- |
| id       | Integer |
| build_id | Integer |
| mod_id   | Integer |

---

# Relaciones

## User → Build

1 : N

Un usuario puede poseer múltiples Builds.

---

## Stock Car → Build

1 : N

Un vehículo base puede utilizarse en múltiples Builds.

---

## Build ↔ Mod

N : M

Implementada mediante la tabla Build Mods.

Una Build puede contener múltiples Mods.

Un Mod puede pertenecer a múltiples Builds.

---

# Validaciones Implementadas

Las entidades utilizan validaciones mediante Pydantic:

* Campos obligatorios.
* Longitudes mínimas y máximas.
* Emails válidos.
* Valores positivos para precios y potencia.
* Restricciones sobre años de producción.
* Verificación de existencia de llaves foráneas.
* Prevención de relaciones duplicadas.
* Protección contra eliminación de registros con dependencias.

---

# Enumeraciones

## FuelType

* Gasoline
* Diesel
* Electric
* Hybrid
* Ethanol
* LPG

---

## ChassisType

* Sedan
* Coupe
* Hatchback
* SUV
* Pickup
* Convertible
* Wagon

---

## BuildApproach

* Street
* Track
* Drift
* Drag
* Offroad
* Show

---

## ModType

* Engine
* Suspension
* Exhaust
* Turbo
* Aerodynamics
* Wheels
* Brakes
* Interior
* Electronics

---

# API REST

## Users

| Método | Endpoint                |
| ------ | ----------------------- |
| GET    | /api/users              |
| GET    | /api/users/{id}         |
| POST   | /api/users              |
| PUT    | /api/users/{id}         |
| DELETE | /api/users/{id}         |
| POST   | /api/users/{id}/picture |

---

## Stock Cars

| Método | Endpoint                     |
| ------ | ---------------------------- |
| GET    | /api/stock-cars              |
| GET    | /api/stock-cars/{id}         |
| POST   | /api/stock-cars              |
| PUT    | /api/stock-cars/{id}         |
| DELETE | /api/stock-cars/{id}         |
| POST   | /api/stock-cars/{id}/picture |

---

## Builds

| Método | Endpoint                       |
| ------ | ------------------------------ |
| GET    | /api/builds                    |
| GET    | /api/builds/{id}               |
| GET    | /api/builds/user/{user_id}     |
| GET    | /api/builds/car/{stock_car_id} |
| POST   | /api/builds                    |
| PUT    | /api/builds/{id}               |
| DELETE | /api/builds/{id}               |
| POST   | /api/builds/{id}/picture       |

---

## Mods

| Método | Endpoint               |
| ------ | ---------------------- |
| GET    | /api/mods              |
| GET    | /api/mods/{id}         |
| POST   | /api/mods              |
| PUT    | /api/mods/{id}         |
| DELETE | /api/mods/{id}         |
| POST   | /api/mods/{id}/picture |

---

## Build Mods

| Método | Endpoint                         |
| ------ | -------------------------------- |
| GET    | /api/build-mods                  |
| GET    | /api/build-mods/build/{build_id} |
| GET    | /api/build-mods/mod/{mod_id}     |
| POST   | /api/build-mods                  |
| PUT    | /api/build-mods/{relation_id}    |
| DELETE | /api/build-mods/{relation_id}    |

---

# Interfaz Web

La aplicación incorpora vistas HTML utilizando Jinja2.

## Módulos Disponibles

* Home
* Users
* Stock Cars
* Builds
* Mods
* Dashboard

---

## Visualizaciones Relacionales

### User Detail

Muestra:

* Información del usuario.
* Builds asociadas al usuario.

### Stock Car Detail

Muestra:

* Información completa del vehículo.
* Builds asociadas al vehículo.

### Build Detail

Muestra:

* Información completa del Build.
* Usuario propietario.
* Vehículo base asociado.
* Mods instalados.

### Mod Detail

Muestra:

* Información completa del Mod.
* Builds que utilizan dicha modificación.

---

# Dashboard Analítico

El sistema incluye un panel estadístico con:

* Top 5 vehículos más utilizados en Builds.
* Top 5 Mods más utilizados.
* Top 5 Builds más costosas.
* Distribución de Build Approaches.
* Distribución de tipos de combustible.
* Gráficos de barras.
* Gráficos de torta.

---

# Almacenamiento de Imágenes

Las imágenes son almacenadas en Supabase Storage.

Cada entidad posee su propio directorio:

```text
users/{id}/
stock-cars/{id}/
builds/{id}/
mods/{id}/
```

---
