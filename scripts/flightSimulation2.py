import requests
import time

# BASE_URL = 'https://openqairamapnapi.qairadrones.com/'
BASE_URL = 'http://0.0.0.0:5000/'
PROCESSED_MEASUREMENT= BASE_URL + '/api/dataProcessed/'


positions = [
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:02.0-05:00",
      "lat":-12.100032, 
      "lon":-77.027007,
      "CO":42.363,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.775,
      "PM25":12.631,
      "PM10":25.046,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100629.10,
      "humidity":72.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:06.0-05:00",
      "lat":-12.101711, 
      "lon":-77.027178,
      "CO":42.505,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.818,
      "PM25":12.816,
      "PM10":25.680,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100622.10,
      "humidity":72.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:10.0-05:00",
      "lat":-12.104312, 
      "lon":-77.027436,
      "CO":42.492,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.858,
      "PM25":13.010,
      "PM10":28.156,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100618.48,
      "humidity":72.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:14.0-05:00",
      "lat":-12.107082, 
      "lon":-77.026835,
      "CO":42.596,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.795,
      "PM25":12.865,
      "PM10":29.391,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100634.78,
      "humidity":73.0,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:18.0-05:00",
      "lat":-12.109516, 
      "lon":-77.026234,
      "CO":42.695,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.762,
      "PM25":12.899,
      "PM10":31.848,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100639.43,
      "humidity":73.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:22.0-05:00",
      "lat":-12.111110, 
      "lon":-77.026148,
      "CO":42.795,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.771,
      "PM25":13.115,
      "PM10":33.658,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100638.39,
      "humidity":73.4,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:32.0-05:00",
      "lat":-12.112537, 
      "lon":-77.026148,
      "CO":42.970,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.821,
      "PM25":13.176,
      "PM10":35.510,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100642.00,
      "humidity":73.5,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:34.0-05:00",
      "lat":-12.114047, 
      "lon":-77.026148,
      "CO":43.031,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.832,
      "PM25":13.403,
      "PM10":37.057,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100639.14,
      "humidity":73.5,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:38.0-05:00",
      "lat":-12.119491, 
      "lon":-77.025762,
      "CO":43.069,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.829,
      "PM25":13.555,
      "PM10":38.014,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100646.13,
      "humidity":73.4,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:42.0-05:00",
      "lat":-12.120058, 
      "lon":-77.025590,
      "CO":43.088,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.854,
      "PM25":13.573,
      "PM10":37.764,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100646.38,
      "humidity":73.3,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:46.0-05:00",
      "lat":-12.120456, 
      "lon":-77.025505,
      "CO":43.106,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.860,
      "PM25":13.530,
      "PM10":38.254,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100645.85,
      "humidity":73.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:50.0-05:00",
      "lat":-12.121002, 
      "lon":-77.025226,
      "CO":43.116,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.841,
      "PM25":13.257,
      "PM10":38.274,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100640.41,
      "humidity":73.0,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:54.0-05:00",
      "lat":-12.122030, 
      "lon":-77.025054,
      "CO":43.117,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.839,
      "PM25":13.239,
      "PM10":39.901,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100639.89,
      "humidity":72.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:19:58.0-05:00",
      "lat":-12.122911, 
      "lon":-77.024775,
      "CO":43.097,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.827,
      "PM25":13.294,
      "PM10":40.500,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100646.85,
      "humidity":72.8,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:02.0-05:00",
      "lat":-12.123603, 
      "lon":-77.024560,
      "CO":43.087,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.867,
      "PM25":13.444,
      "PM10":40.542,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100641.93,
      "humidity":72.7,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:06.0-05:00",
      "lat":-12.124212, 
      "lon":-77.024432,
      "CO":43.082,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.832,
      "PM25":13.426,
      "PM10":41.007,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100635.46,
      "humidity":72.7,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:10.0-05:00",
      "lat":-12.125177, 
      "lon":-77.024196,
      "CO":43.089,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.811,
      "PM25":13.235,
      "PM10":39.755,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100641.41,
      "humidity":72.7,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:14.0-05:00",
      "lat":-12.126268, 
      "lon":-77.023852,
      "CO":43.117,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.825,
      "PM25":13.362,
      "PM10":40.350,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100635.44,
      "humidity":72.7,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:18.0-05:00",
      "lat":-12.127422, 
      "lon":-77.023552,
      "CO":42.861,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.850,
      "PM25":13.606,
      "PM10":41.360,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100637.50,
      "humidity":72.8,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:22.0-05:00",
      "lat":-12.126645,
      "lon": -77.023831,
      "CO":43.009,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.849,
      "PM25":13.413,
      "PM10":40.773,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100639.31,
      "humidity":72.8,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:28.0-05:00",
      "lat":-12.127484, 
      "lon":-77.023466,
      "CO":42.879,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.831,
      "PM25":13.249,
      "PM10":41.270,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100635.67,
      "humidity":72.8,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:30.0-05:00",
      "lat":-12.128450, 
      "lon":-77.023166,
      "CO":42.644,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.882,
      "PM25":13.293,
      "PM10":40.608,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100643.18,
      "humidity":72.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:34.0-05:00",
      "lat":-12.129708, 
      "lon":-77.022801,
      "CO":42.828,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.857,
      "PM25":12.980,
      "PM10":38.152,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100638.77,
      "humidity":72.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:38.0-05:00",
      "lat":-12.131114, 
      "lon":-77.022286,
      "CO":42.756,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.842,
      "PM25":12.857,
      "PM10":36.398,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100640.31,
      "humidity":72.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:42.0-05:00",
      "lat":-12.132289, 
      "lon":-77.021878,
      "CO":42.817,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.838,
      "PM25":12.955,
      "PM10":36.788,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100636.41,
      "humidity":73.0,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:46.0-05:00",
      "lat":-12.133065, 
      "lon":-77.021342,
      "CO":42.892,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.805,
      "PM25":12.933,
      "PM10":36.553,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100629.15,
      "humidity":73.0,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:50.0-05:00",
      "lat":-12.133799, 
      "lon":-77.021234,
      "CO":42.937,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.867,
      "PM25":13.025,
      "PM10":36.101,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100625.04,
      "humidity":73.0,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:54.0-05:00",
      "lat":-12.134491, 
      "lon":-77.021814,
      "CO":42.810,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.953,
      "PM25":13.176,
      "PM10":35.893,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100632.39,
      "humidity":72.8,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:20:58.0-05:00",
      "lat":-12.135052, 
      "lon":-77.022726,
      "CO":42.494,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.962,
      "PM25":13.130,
      "PM10":36.023,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100636.10,
      "humidity":72.3,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:02.0-05:00",
      "lat":-12.135566, 
      "lon":-77.023638,
      "CO":41.992,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.920,
      "PM25":12.992,
      "PM10":35.259,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100650.10,
      "humidity":71.8,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:06.0-05:00",
      "lat":-12.135797, 
      "lon":-77.024196,
      "CO":41.343,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.931,
      "PM25":13.130,
      "PM10":36.073,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100643.67,
      "humidity":71.5,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:10.0-05:00",
      "lat":-12.136038, 
      "lon":-77.024893,
      "CO":40.542,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.959,
      "PM25":13.248,
      "PM10":35.348,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100640.34,
      "humidity":71.3,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:14.0-05:00",
      "lat":-12.136259, 
      "lon":-77.025472,
      "CO":39.542,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.939,
      "PM25":13.110,
      "PM10":35.115,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100650.43,
      "humidity":71.2,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:18.0-05:00",
      "lat":-12.136657, 
      "lon":-77.025934,
      "CO":38.374,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.937,
      "PM25":13.226,
      "PM10":35.920,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100644.21,
      "humidity":71.2,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:22.0-05:00",
      "lat":-12.136982, 
      "lon":-77.026127,
      "CO":37.041,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.961,
      "PM25":13.271,
      "PM10":35.913,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.1,
      "pressure":100653.98,
      "humidity":71.2,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:28.0-05:00",
      "lat":-12.137413, 
      "lon":-77.026406,
      "CO":35.944,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.000,
      "PM25":13.529,
      "PM10":36.987,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100664.76,
      "humidity":71.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:30.0-05:00",
      "lat":-12.137926, 
      "lon":-77.026867,
      "CO":34.443,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.069,
      "PM25":13.683,
      "PM10":39.459,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100668.58,
      "humidity":71.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:34.0-05:00",
      "lat":-12.138430, 
      "lon":-77.026867,
      "CO":32.677,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.130,
      "PM25":13.775,
      "PM10":41.847,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100664.32,
      "humidity":71.2,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:38.0-05:00",
      "lat":-12.138986, 
      "lon":-77.027146,
      "CO":30.790,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.168,
      "PM25":13.861,
      "PM10":41.203,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100659.78,
      "humidity":71.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:42.0-05:00",
      "lat":-12.138996, 
      "lon":-77.027768,
      "CO":28.762,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.183,
      "PM25":13.846,
      "PM10":37.891,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100664.76,
      "humidity":71.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:46.0-05:00",
      "lat":-12.138073, 
      "lon":-77.028176,
      "CO":26.552,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.178,
      "PM25":13.986,
      "PM10":39.469,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100675.48,
      "humidity":71.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:50.0-05:00",
      "lat":-12.137413, 
      "lon":-77.028455,
      "CO":24.496,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.212,
      "PM25":14.099,
      "PM10":40.290,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":23.0,
      "pressure":100667.25,
      "humidity":71.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:54.0-05:00",
      "lat":-12.136479, 
      "lon":-77.028895,
      "CO":22.476,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.213,
      "PM25":14.045,
      "PM10":40.244,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.9,
      "pressure":100670.41,
      "humidity":71.0,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:21:58.0-05:00",
      "lat":-12.135755, 
      "lon":-77.029185,
      "CO":20.265,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.215,
      "PM25":14.021,
      "PM10":38.727,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.9,
      "pressure":100674.29,
      "humidity":71.0,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:02.0-05:00",
      "lat":-12.135210, 
      "lon":-77.029356,
      "CO":18.352,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.188,
      "PM25":13.873,
      "PM10":36.632,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.8,
      "pressure":100686.13,
      "humidity":71.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:06.0-05:00",
      "lat":-12.134329, 
      "lon":-77.029732,
      "CO":16.472,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.100,
      "PM25":13.548,
      "PM10":36.079,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.8,
      "pressure":100685.86,
      "humidity":71.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:10.0-05:00",
      "lat":-12.133647, 
      "lon":-77.030172,
      "CO":14.362,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.050,
      "PM25":13.429,
      "PM10":35.924,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.8,
      "pressure":100693.05,
      "humidity":71.2,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:14.0-05:00",
      "lat":-12.133259, 
      "lon":-77.030526,
      "CO":12.433,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.064,
      "PM25":13.617,
      "PM10":36.407,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.8,
      "pressure":100696.07,
      "humidity":71.3,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:18.0-05:00",
      "lat":-12.132525, 
      "lon":-77.031384,
      "CO":10.810,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.108,
      "PM25":13.687,
      "PM10":36.737,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.7,
      "pressure":100705.39,
      "humidity":71.4,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:22.0-05:00",
      "lat":-12.131843, 
      "lon":-77.032253,
      "CO":8.914,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.083,
      "PM25":13.501,
      "PM10":35.732,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.7,
      "pressure":100710.59,
      "humidity":71.5,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:27.0-05:00",
      "lat":-12.131371, 
      "lon":-77.033347,
      "CO":7.339,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.082,
      "PM25":13.427,
      "PM10":34.978,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.6,
      "pressure":100700.09,
      "humidity":71.6,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:30.0-05:00",
      "lat":-12.130857, 
      "lon":-77.034570,
      "CO":5.828,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.122,
      "PM25":13.602,
      "PM10":35.233,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.6,
      "pressure":100694.49,
      "humidity":71.7,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:34.0-05:00",
      "lat":-12.130259, 
      "lon":-77.035182,
      "CO":4.114,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.104,
      "PM25":13.465,
      "PM10":34.379,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.6,
      "pressure":100687.35,
      "humidity":71.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:38.0-05:00",
      "lat":-12.129493, 
      "lon":-77.035675,
      "CO":2.904,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.099,
      "PM25":13.288,
      "PM10":33.744,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.5,
      "pressure":100670.65,
      "humidity":72.0,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:42.0-05:00",
      "lat":-12.129000, 
      "lon":-77.036008,
      "CO":1.296,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":5.061,
      "PM25":13.087,
      "PM10":32.994,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.5,
      "pressure":100675.05,
      "humidity":72.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:46.0-05:00",
      "lat":-12.128213, 
      "lon":-77.036469,
      "CO":0.252,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.974,
      "PM25":12.862,
      "PM10":29.176,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.4,
      "pressure":100672.25,
      "humidity":72.2,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:50.0-05:00",
      "lat":-12.127657, 
      "lon":-77.036866,
      "CO":0,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.878,
      "PM25":12.704,
      "PM10":27.904,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.4,
      "pressure":100662.96,
      "humidity":72.4,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:54.0-05:00",
      "lat":-12.127123, 
      "lon":-77.037134,
      "CO":0,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.831,
      "PM25":12.747,
      "PM10":28.444,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.3,
      "pressure":100656.27,
      "humidity":72.6,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:22:58.0-05:00",
      "lat":-12.126420, 
      "lon":-77.037724,
      "CO":0,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.794,
      "PM25":12.603,
      "PM10":28.214,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.3,
      "pressure":100645.49,
      "humidity":72.8,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:23:02.0-05:00",
      "lat":-12.125916, 
      "lon":-77.038304,
      "CO":0,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.801,
      "PM25":12.441,
      "PM10":26.178,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.2,
      "pressure":100637.52,
      "humidity":72.9,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:23:06.0-05:00",
      "lat":-12.125371, 
      "lon":-77.038905,
      "CO":0,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.798,
      "PM25":12.400,
      "PM10":25.920,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.2,
      "pressure":100641.17,
      "humidity":73.1,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:23:10.0-05:00",
      "lat":-12.125035, 
      "lon":-77.039420,
      "CO":0,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.823,
      "PM25":12.583,
      "PM10":27.293,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.1,
      "pressure":100642.82,
      "humidity":73.3,
      "VOC":0.003,
      "CO2":30.0
   },
   {
      "ID":"qH058",
      "timestamp":"2020-12-10 18:23:14.0-05:00",
      "lat":-12.124364, 
      "lon":-77.040621,
      "CO":0,
      "H2S":0,
      "NO2":0,
      "O3":0,
      "SO2":0,
      "PM1":4.855,
      "PM25":12.718,
      "PM10":28.552,
      "UV":0,
      "UVA":0,
      "UVB":0,
      "spl":0,
      "temperature":22.1,
      "pressure":100652.24,
      "humidity":73.5,
      "VOC":0.003,
      "CO2":30.0
   }
]

for pos in positions:
	response_measurement = requests.post(PROCESSED_MEASUREMENT, json=pos)
	time.sleep(5)



