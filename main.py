from jinja2 import Environment, FileSystemLoader

pages = [
    {
        'name': 'index',
        'shows': [
            {
                'name': 'Keys to the Lodge',
                'image': 'keys',
                'description': 'Data driven commentary on 2019 Australian federal elections.',
                'new': True,
                'link': {
                    'url': 'https://pod.link/1447060366',
                    'disabled': False,
                    'title': 'Subscribe'
                },
            },
            {
                'name': 'Aus Pol Stats',
                'image': 'aps',
                'type': 'Website',
                'description': 'Australian Politics Statistics, tracked daily.',
                'new': False,
                'link': {
                    'url': 'https://twitter.com/AusPolStats?lang=en',
                    'disabled': False,
                    'title': 'Twitter'
                },
                'link2': {
                    'url': 'https://auspolstats.com',
                    'disabled': False,
                    'title': 'Website'
                },
            },
            {
                'name': 'Backbench Bandits',
                'image': 'backbench',
                'description': 'Hot takes on Australian politics scandals.',
                'link': {
                    'url': 'https://pod.link/1433761688',
                    'disabled': False,
                    'title': 'Subscribe'
                },
            },
            {
                'name': 'The Choice Less Chosen',
                'image': 'choice',
                'description': 'Exploring the world of choose-your-own-adventure books.',
                'link': {
                    'url': 'https://pod.link/1220812943',
                    'disabled': False,
                    'title': 'Subscribe'
                },
            },
            {
                'name': 'Podblaster',
                'image': 'podblasters',
                'description': 'Join friends on a quest to find out what makes a good podcast.',
                'link': {
                    'url': 'https://pod.link/1187823014',
                    'disabled': False,
                    'title': 'Subscribe'
                },
            },
            {
                'name': 'PyAndy',
                'image': 'pyandy',
                'type': 'Videos',
                'description': 'Live streamed python programming.',
                'new': False,
                'link': {
                    'url': 'https://www.youtube.com/channel/UCT0oEArSloMLL_URLyy2HfA',
                    'disabled': False,
                    'title': 'YouTube'
                },
            },
        ]
    },
    {
        'name': 'contact',
    },
]


def render():
    env = Environment(
        loader=FileSystemLoader('templates'),
    )

    for page in pages:
        template = env.get_template(f'{page["name"]}.html.j2')

        with open(f'{page["name"]}.html', 'w') as output_file:
            output_file.write(template.render(page=page))


if __name__ == '__main__':
    render()
