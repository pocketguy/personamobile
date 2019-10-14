import random

from django.core.files import File as DjangoFile
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Factory, File, Post, Project
from ...util import gen_image


class Command(BaseCommand):
    help = "Fills database with fake data"

    def handle(self, *args, **options):
        random.seed(42)
        fake = Faker("ru-RU")

        Factory.objects.all().delete()
        File.objects.all().delete()
        Post.objects.all().delete()
        Project.objects.all().delete()

        files = []
        for _ in range(10):
            img = DjangoFile(gen_image())
            f = File.objects.create(file=img, description=fake.sentence()[:-1])
            files.append(f)

        factories = []
        for _ in range(10):
            f = Factory.objects.create(
                name=fake.sentence(3)[:-1],
                description=fake.text(),
                cover=random.choice(files),
            )
            factories.append(f)

        projects = []
        for _ in range(10):
            p = Project.objects.create(
                name=fake.sentence(3)[:-1],
                description=fake.text(),
                cover=random.choice(files),
            )
            projects.append(p)

        posts = []
        for _ in range(random.randrange(30, 100)):
            text = ""
            text += f"<p>{fake.paragraph()}</p>"
            text += "<ul>"
            for _ in range(random.randrange(3, 7)):
                text += f"<li>{fake.sentence()}</li>"
            text += "</ul>"
            text += f"<p>{fake.paragraph()}</p>"
            text += f"<h2>{fake.paragraph()}</h2>"
            text += f"<p>{fake.paragraph()}</p>"
            text += "<ol>"
            for _ in range(random.randrange(3, 7)):
                text += f"<li>{fake.sentence()}</li>"
            text += "</ol>"
            text += f"<h2>{fake.paragraph()}</h2>"
            text += f"<p>{fake.paragraph()}</p>"
            text += f"<blockquote>{fake.paragraph()}</blockquote>"
            text += f"<p>{fake.paragraph()}</p>"

            seo_title = ""
            seo_description = ""

            if random.choice([True, False]):
                seo_title = fake.sentence()
                seo_description = fake.text()

            p = Post.objects.create(
                title=fake.sentence()[:-1],
                text=text,
                cover=random.choice(files),
                seo_title=seo_title,
                seo_description=seo_description,
            )
            posts.append(p)
