from jinja2 import Environment, FileSystemLoader

pages = [
    {
        'name': 'home',
        'shows': [
            {
                'name': 'Keys to the Lodge',
                'image': 'keys',
                'description': 'Data driven commentary on 2019 Australian federal elections.',
                'new': True,
                'link': '#',
            },
            {
                'name': 'Backbench Bandits',
                'image': 'backbench',
                'description': 'Hot takes on Australian politics scandals.',
                'link': 'https://pod.link/1433761688',
            },
            {
                'name': 'The Choice Less Chosen',
                'image': 'choice',
                'description': 'Exploring the world of choose-your-own-adventure books.',
                'link': 'https://pod.link/1220812943',
            },
            {
                'name': 'Podblaster',
                'image': 'podblasters',
                'description': 'Join friends on a quest to find out what makes a good podcast.',
                'link': 'https://pod.link/1187823014',
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
