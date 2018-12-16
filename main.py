from jinja2 import Environment, FileSystemLoader

pages = [
    {
        'name': 'home'
    },
    {
        'name': 'shows',
        'shows': [
            {
                'name': 'Podblaster',
                'image': 'podblasters',
                'description': 'Leading the charge of podcast innovation, the team discusses ' +
                               'podcasting ideas for the future.'
            },
            {
                'name': 'Backbench Bandits',
                'image': 'backbench',
                'description': 'Politics taken lightly'
            },
        ]
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
