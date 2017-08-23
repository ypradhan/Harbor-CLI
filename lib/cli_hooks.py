''' All CLI hooks are handled through here. '''
import sys

from lib.services import deploy_service, registration_service
from lib.services.firebase_service import Firebase
from lib.services.builder_service import builder
from lib.constants.release_types import ReleaseTypes

import click

@click.group()
def cli():
    ''' CLI for the Harbor application. '''
    pass


@click.command()
@click.option('-u', is_flag=True, help='Flag to indicate if a user is to be registered.')
def register(u):
    ''' Register your project/user on the server. '''
    registration_service.RegistrationService(
        Firebase(),
        Firebase()
    ).delegate(True if u else False)


@click.command()
@click.option('--type', help='Release type [qa, uat, dev]. This affects the audience that receives notice of this release. Default value of "dev" is assumed')
def deploy(type):
    ''' Deploy your project once it has been registered. '''
    if type is None:
        type = ReleaseTypes.DEV.value

    if type.lower() not in [release_type.value.lower() for release_type in ReleaseTypes]:
        print('{0} is not a valid release type. Please use "uat", "qa" or "dev".'.format(type))
        sys.exit(1)

    deploy_service.DeployService(
        type,
        Firebase(),
        Firebase(),
        builder()()
    ).delegate()


cli.add_command(register)
cli.add_command(deploy)
