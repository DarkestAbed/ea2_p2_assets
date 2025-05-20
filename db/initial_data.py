# db/initial_data.py

SUCURSALES: list[dict] = [
    {
        "id": "SC001",
        "localidad": "Las Condes"
    },
    {
        "id": "SC002",
        "localidad": "Ñuñoa"
    },
    {
        "id": "SC003",
        "localidad": "Maipú"
    },
    {
        "id": "SC004",
        "localidad": "Providencia"
    },
    {
        "id": "SC005",
        "localidad": "Viña del Mar"
    },
    {
        "id": "SC006",
        "localidad": "Concepción"
    },
    {
        "id": "SC007",
        "localidad": "La Serena"
    }
]

VENDEDORES: list[dict] = [
    {
        "id": "V001",
        "nombre": "Ana Flores",
        "email": "ana.flores@ferremas.cl",
        "sucursal": "SC001"
    },
    {
        "id": "V002",
        "nombre": "Pedro Soto",
        "email": "pedro.soto@ferremas.cl",
        "sucursal": "SC001"
    },
    {
        "id": "V003",
        "nombre": "Carolina Rojas",
        "email": "carolina.rojas@ferremas.cl",
        "sucursal": "SC001"
    },
    {
        "id": "V004",
        "nombre": "Miguel Ángel",
        "email": "miguel.angel@ferremas.cl",
        "sucursal": "SC002"
    },
    {
        "id": "V005",
        "nombre": "Sofía Morales",
        "email": "sofia.morales@ferremas.cl",
        "sucursal": "SC002"
    },
    {
        "id": "V006",
        "nombre": "Javier Bustos",
        "email": "javier.bustos@ferremas.cl",
        "sucursal": "SC002"
    },
    {
        "id": "V007",
        "nombre": "Daniela Vera",
        "email": "daniela.vera@ferremas.cl",
        "sucursal": "SC003"
    },
    {
        "id": "V008",
        "nombre": "Ricardo Pérez",
        "email": "ricardo.perez@ferremas.cl",
        "sucursal": "SC003"
    },
    {
        "id": "V009",
        "nombre": "Paula Castro",
        "email": "paula.castro@ferremas.cl",
        "sucursal": "SC003"
    },
    {
        "id": "V010",
        "nombre": "Felipe Herrera",
        "email": "felipe.herrera@ferremas.cl",
        "sucursal": "SC004"
    },
    {
        "id": "V011",
        "nombre": "Isidora Soto",
        "email": "isidora.soto@ferremas.cl",
        "sucursal": "SC004"
    },
    {
        "id": "V012",
        "nombre": "Gonzalo Díaz",
        "email": "gonzalo.diaz@ferremas.cl",
        "sucursal": "SC004"
    },
    {
        "id": "V013",
        "nombre": "Andrea Loyola",
        "email": "andrea.loyola@ferremas.cl",
        "sucursal": "SC005"
    },
    {
        "id": "V014",
        "nombre": "Juan Cárdenas",
        "email": "juan.cardenas@ferremas.cl",
        "sucursal": "SC005"
    },
    {
        "id": "V015",
        "nombre": "Bernardita Rojas",
        "email": "bernardita.rojas@ferremas.cl",
        "sucursal": "SC005"
    },
    {
        "id": "V016",
        "nombre": "Carlos Gómez",
        "email": "carlos.gomez@ferremas.cl",
        "sucursal": "SC006"
    },
    {
        "id": "V017",
        "nombre": "Laura Valdés",
        "email": "laura.valdes@ferremas.cl",
        "sucursal": "SC006"
    },
    {
        "id": "V018",
        "nombre": "Roberto Fuentes",
        "email": "roberto.fuentes@ferremas.cl",
        "sucursal": "SC006"
    },
    {
        "id": "V019",
        "nombre": "María José Salinas",
        "email": "maria.salinas@ferremas.cl",
        "sucursal": "SC007"
    },
    {
        "id": "V020",
        "nombre": "Jorge Vidal",
        "email": "jorge.vidal@ferremas.cl",
        "sucursal": "SC007"
    },
    {
        "id": "V021",
        "nombre": "Romina Tapia",
        "email": "romina.tapia@ferremas.cl",
        "sucursal": "SC007"
    }
]

ARTICULOS: list[dict] = [
    {
        "id": "ART001",
        "categoria": "Herramientas Manuales",
        "subcategoria": "Martillos y Mazos",
        "nombre": "Martillo de uña 16 oz",
        "marca": "Stanley",
        "precio": 8990,
        "stock": 150
    },
    {
        "id": "ART002",
        "categoria": "Herramientas Manuales",
        "subcategoria": "Destornilladores",
        "nombre": "Set destornilladores phillips y planos (6 piezas)",
        "marca": "Pretul",
        "precio": 12500,
        "stock": 200
    },
    {
        "id": "ART003",
        "categoria": "Herramientas Eléctricas",
        "subcategoria": "Taladros",
        "nombre": "Taladro percutor 750W",
        "marca": "Bosch",
        "precio": 45990,
        "stock": 80
    },
    {
        "id": "ART004",
        "categoria": "Herramientas Eléctricas",
        "subcategoria": "Esmeriles",
        "nombre": "Esmeril angular 4 1/2''",
        "marca": "Black+Decker",
        "precio": 32990,
        "stock": 70
    },
    {
        "id": "ART005",
        "categoria": "Ferretería General",
        "subcategoria": "Tornillería",
        "nombre": "Caja surtida de tornillos para madera (200 unidades)",
        "marca": "Fixer",
        "precio": 5500,
        "stock": 300
    },
    {
        "id": "ART006",
        "categoria": "Ferretería General",
        "subcategoria": "Adhesivos y Selladores",
        "nombre": "Silicona multiuso transparente",
        "marca": "Sika",
        "precio": 3200,
        "stock": 180
    },
    {
        "id": "ART007",
        "categoria": "Jardinería",
        "subcategoria": "Herramientas de Jardín",
        "nombre": "Tijera de podar bypass",
        "marca": "Bellota",
        "precio": 9800,
        "stock": 120
    },
    {
        "id": "ART008",
        "categoria": "Jardinería",
        "subcategoria": "Riego",
        "nombre": "Manguera de jardín 20 metros con acoples",
        "marca": "Gardena",
        "precio": 18990,
        "stock": 90
    },
    {
        "id": "ART009",
        "categoria": "Fontanería",
        "subcategoria": "Grifería",
        "nombre": "Grifo de lavaplatos monomando",
        "marca": "Wasser",
        "precio": 29990,
        "stock": 60
    },
    {
        "id": "ART010",
        "categoria": "Fontanería",
        "subcategoria": "Conexiones y Tuberías",
        "nombre": "Kit de reparación de fugas (cintas y abrazaderas)",
        "marca": "Tricoflex",
        "precio": 7500,
        "stock": 110
    },
    {
        "id": "ART011",
        "categoria": "Pintura",
        "subcategoria": "Pinturas Interior",
        "nombre": "Látex interior blanco 1 galón",
        "marca": "Sipa",
        "precio": 15990,
        "stock": 75
    },
    {
        "id": "ART012",
        "categoria": "Pintura",
        "subcategoria": "Accesorios de Pintura",
        "nombre": "Set de brochas y rodillo (5 piezas)",
        "marca": "Kolor",
        "precio": 6500,
        "stock": 130
    },
    {
        "id": "ART013",
        "categoria": "Electricidad",
        "subcategoria": "Cables y Alambres",
        "nombre": "Cable eléctrico 2x1.5mm (20 metros)",
        "marca": "Cenel",
        "precio": 11200,
        "stock": 95
    },
    {
        "id": "ART014",
        "categoria": "Electricidad",
        "subcategoria": "Materiales Eléctricos",
        "nombre": "Set de enchufes y interruptores (10 unidades)",
        "marca": "BTicino",
        "precio": 8900,
        "stock": 160
    },
    {
        "id": "ART015",
        "categoria": "Seguridad",
        "subcategoria": "Candados y Cierres",
        "nombre": "Candado de seguridad con combinación",
        "marca": "Yale",
        "precio": 4500,
        "stock": 220
    },
    {
        "id": "ART016",
        "categoria": "Herramientas Manuales",
        "subcategoria": "Llaves",
        "nombre": "Set de llaves mixtas (12 piezas)",
        "marca": "Force",
        "precio": 21500,
        "stock": 100
    },
    {
        "id": "ART017",
        "categoria": "Herramientas Manuales",
        "subcategoria": "Alicates y Cortadores",
        "nombre": "Alicate universal 8 pulgadas",
        "marca": "Bahco",
        "precio": 7800,
        "stock": 190
    },
    {
        "id": "ART018",
        "categoria": "Herramientas Eléctricas",
        "subcategoria": "Sierras",
        "nombre": "Sierra caladora 500W",
        "marca": "Makita",
        "precio": 52000,
        "stock": 65
    },
    {
        "id": "ART019",
        "categoria": "Herramientas Eléctricas",
        "subcategoria": "Lijadoras",
        "nombre": "Lijadora orbital 240W",
        "marca": "Dewalt",
        "precio": 38000,
        "stock": 70
    },
    {
        "id": "ART020",
        "categoria": "Ferretería General",
        "subcategoria": "Fijaciones",
        "nombre": "Tarugos y tornillos para concreto (50 unidades)",
        "marca": "Fischer",
        "precio": 4200,
        "stock": 250
    },
    {
        "id": "ART021",
        "categoria": "Ferretería General",
        "subcategoria": "Cintas Adhesivas",
        "nombre": "Cinta métrica 5 metros",
        "marca": "Truper",
        "precio": 3500,
        "stock": 280
    },
    {
        "id": "ART022",
        "categoria": "Jardinería",
        "subcategoria": "Cultivo",
        "nombre": "Pala de punta redonda",
        "marca": "Herragro",
        "precio": 11500,
        "stock": 85
    },
    {
        "id": "ART023",
        "categoria": "Jardinería",
        "subcategoria": "Maquinaria de Jardín",
        "nombre": "Cortacésped eléctrico 1200W",
        "marca": "Einhell",
        "precio": 79990,
        "stock": 40
    },
    {
        "id": "ART024",
        "categoria": "Fontanería",
        "subcategoria": "Bombas de Agua",
        "nombre": "Bomba de agua periférica 0.5 HP",
        "marca": "Shimge",
        "precio": 65000,
        "stock": 30
    },
    {
        "id": "ART025",
        "categoria": "Fontanería",
        "subcategoria": "Fittings PVC",
        "nombre": "Codo PVC 90° 1/2 pulgada (10 unidades)",
        "marca": "Duratec",
        "precio": 2800,
        "stock": 400
    },
    {
        "id": "ART026",
        "categoria": "Pintura",
        "subcategoria": "Pinturas Exterior",
        "nombre": "Esmalte sintético blanco 1/4 galón",
        "marca": "Chilecolor",
        "precio": 7200,
        "stock": 90
    },
    {
        "id": "ART027",
        "categoria": "Pintura",
        "subcategoria": "Preparación de Superficies",
        "nombre": "Espátula de acero inoxidable 3 pulgadas",
        "marca": "Wolfcraft",
        "precio": 2500,
        "stock": 170
    },
    {
        "id": "ART028",
        "categoria": "Electricidad",
        "subcategoria": "Iluminación",
        "nombre": "Ampolleta LED E27 10W luz cálida",
        "marca": "Philips",
        "precio": 1990,
        "stock": 500
    },
    {
        "id": "ART029",
        "categoria": "Electricidad",
        "subcategoria": "Herramientas de Electricista",
        "nombre": "Tester digital multímetro",
        "marca": "Fluke",
        "precio": 19990,
        "stock": 50
    },
    {
        "id": "ART030",
        "categoria": "Seguridad",
        "subcategoria": "Equipos de Protección Personal",
        "nombre": "Guantes de seguridad anticorte",
        "marca": "Ansell",
        "precio": 3800,
        "stock": 250
    },
    {
        "id": "ART031",
        "categoria": "Herramientas Manuales",
        "subcategoria": "Niveles",
        "nombre": "Nivel de burbuja 60 cm",
        "marca": "Stabila",
        "precio": 15000,
        "stock": 80
    },
    {
        "id": "ART032",
        "categoria": "Herramientas Eléctricas",
        "subcategoria": "Atornilladores",
        "nombre": "Atornillador inalámbrico 12V",
        "marca": "Milwaukee",
        "precio": 58000,
        "stock": 55
    },
    {
        "id": "ART033",
        "categoria": "Ferretería General",
        "subcategoria": "Clavos y Remaches",
        "nombre": "Caja de clavos surtidos (1 kg)",
        "marca": "Aceros Aza",
        "precio": 3900,
        "stock": 180
    },
    {
        "id": "ART034",
        "categoria": "Jardinería",
        "subcategoria": "Fertilizantes y Sustratos",
        "nombre": "Tierra de hojas premium (25 litros)",
        "marca": "Anasac",
        "precio": 6500,
        "stock": 100
    },
    {
        "id": "ART035",
        "categoria": "Fontanería",
        "subcategoria": "Calefont y Termos",
        "nombre": "Calefont tiro forzado 10 litros",
        "marca": "Junkers",
        "precio": 180000,
        "stock": 25
    },
    {
        "id": "ART036",
        "categoria": "Pintura",
        "subcategoria": "Impermeabilizantes",
        "nombre": "Impermeabilizante acrílico para techos 1 galón",
        "marca": "Volcán",
        "precio": 25000,
        "stock": 45
    },
    {
        "id": "ART037",
        "categoria": "Electricidad",
        "subcategoria": "Extensores y Enrolladores",
        "nombre": "Extensor eléctrico 5 metros (3 tomas)",
        "marca": "Legrand",
        "precio": 9500,
        "stock": 140
    },
    {
        "id": "ART038",
        "categoria": "Seguridad",
        "subcategoria": "Alarmas y Detectores",
        "nombre": "Detector de humo autónomo",
        "marca": "Kidde",
        "precio": 7900,
        "stock": 90
    },
    {
        "id": "ART039",
        "categoria": "Herramientas Manuales",
        "subcategoria": "Sierras Manuales",
        "nombre": "Serrucho costilla 12 pulgadas",
        "marca": "Stanley",
        "precio": 6800,
        "stock": 130
    },
    {
        "id": "ART040",
        "categoria": "Ferretería General",
        "subcategoria": "Limpieza y Desengrasantes",
        "nombre": "Desengrasante industrial 1 litro",
        "marca": "CRC",
        "precio": 4500,
        "stock": 110
    },
    {
        "id": "ART041",
        "categoria": "Jardinería",
        "subcategoria": "Semillas",
        "nombre": "Semillas de césped premium (1 kg)",
        "marca": "Terrafertil",
        "precio": 9000,
        "stock": 70
    },
    {
        "id": "ART042",
        "categoria": "Fontanería",
        "subcategoria": "Accesorios de Baño",
        "nombre": "Flexible de ducha 1.5 metros",
        "marca": "Fanaloza",
        "precio": 5200,
        "stock": 160
    }
]