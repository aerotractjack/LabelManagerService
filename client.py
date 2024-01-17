import requests
from LabelService.aoi_gen import gen_aois

url = "http://192.168.1.35:7112/gen_aois"

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", "-c", required=True, help="Client ID")
    parser.add_argument("--project", "-p", required=True, help="Project ID")
    parser.add_argument("--stand", "-s", required=True, help="Stand 3-Digit ID", nargs="+")
    args = parser.parse_args()

    for stand in args.stand:
        msg = f"Starting {args.client}, {args.project}, {stand}"
        print(msg)
        contents = {
            "CLIENT_ID": args.client, 
            "PROJECT_ID": args.project, 
            "STAND_ID": stand
        }
        req = requests.post(url, json=contents, timeout=(60*5, 60*5))
        print(req)
        print(req.text)
        print("=============")