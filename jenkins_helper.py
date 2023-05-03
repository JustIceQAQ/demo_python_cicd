import argparse
import jenkins


def main(uri: str, account: str, password: str, job_name: str, build_number: int = None):
    server = jenkins.Jenkins(uri, username=account, password=password)
    latest_build_number = server.get_job_info(job_name)['nextBuildNumber'] - 1 if build_number is None else build_number
    server.stop_build(job_name, latest_build_number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Python Call Jenkins Script.")
    parser.add_argument('-u', '--uri', help='Jenkins URI', required=True)
    parser.add_argument('-a', '--account', help='Jenkins Login Account', required=True)
    parser.add_argument('-p', '--password', help='Jenkins Login Password', required=True)
    parser.add_argument('-n', '--job-name', help='Jenkins Job Mame', required=True)
    parser.add_argument('-num', '--build-number', help='Jenkins Job Build Number (Auto Get Latest Build Number)')
    args = parser.parse_args().__dict__
    main(**args)
