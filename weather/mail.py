import json


json_data = '''
{
    "photos": [
        {
            "id": 102693,
            "sol": 1000,
            "camera": {
                "id": 20,
                "name": "FHAZ",
                "rover_id": 5,
                "full_name": "Front Hazard Avoidance Camera"
            },
            "img_src": "http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG",
            "earth_date": "2015-05-30",
            "rover": {
                "id": 5,
                "name": "Curiosity",
                "landing_date": "2012-08-06",
                "launch_date": "2011-11-26",
                "status": "active",
                "max_sol": 4102,
                "max_date": "2024-02-19",
                "total_photos": 695670,
                "cameras": [
                    {
                        "name": "FHAZ",
                        "full_name": "Front Hazard Avoidance Camera"
                    },
                    {
                        "name": "NAVCAM",
                        "full_name": "Navigation Camera"
                    },
                    {
                        "name": "MAST",
                        "full_name": "Mast Camera"
                    },
                    {
                        "name": "CHEMCAM",
                        "full_name": "Chemistry and Camera Complex"
                    },
                    {
                        "name": "MAHLI",
                        "full_name": "Mars Hand Lens Imager"
                    },
                    {
                        "name": "MARDI",
                        "full_name": "Mars Descent Imager"
                    },
                    {
                        "name": "RHAZ",
                        "full_name": "Rear Hazard Avoidance Camera"
                    }
                ]
            }
        }
    ]
}
'''
data = data = json.loads(json_data)

for sample in data:
    print(sample["photos"]["id"])
    

    
    
