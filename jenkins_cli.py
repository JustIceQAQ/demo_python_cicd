import click
import jenkins


# pip install python-jenkins

@click.group()
def jenkins_cli():
    pass


@jenkins_cli.command()
@click.option('-u', "--uri", help="Jenkins URI", required=True, type=str)
@click.option('-a', "--account", help="Jenkins Login Account", required=True, type=str)
@click.option('-p', "--password", help="Jenkins Login Password", required=True, type=str)
@click.option('-n', "--job-name", help="Jenkins Job Mame", required=True, type=str)
@click.option("--build-number", help="Jenkins Job Build Number (Auto Get Latest Build Number)", type=str)
def stop_build(uri, account, password, job_name, build_number):
    server = jenkins.Jenkins(uri, username=account, password=password)
    latest_build_number = (
        server.get_job_info(job_name)['nextBuildNumber'] - 1
        if build_number is None
        else build_number
    )
    server.stop_build(job_name, latest_build_number)


@jenkins_cli.command()
@click.option('-u', "--uri", help="Jenkins URI", required=True, type=str)
@click.option('-a', "--account", help="Jenkins Login Account", required=True, type=str)
@click.option('-p', "--password", help="Jenkins Login Password", required=True, type=str)
@click.option('-n', "--job-name", help="Jenkins Job Mame", required=True, type=str)
def run_build(uri, account, password, job_name):
    server = jenkins.Jenkins(uri, username=account, password=password)
    server.build_job(job_name)


cli = click.CommandCollection(sources=[jenkins_cli])

if __name__ == '__main__':
    cli()
