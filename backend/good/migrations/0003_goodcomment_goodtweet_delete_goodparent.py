# Generated by Django 4.0 on 2023-01-14 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_alter_tweet_good_count_alter_tweet_user_id_and_more'),
        ('comment', '0001_initial'),
        ('good', '0002_remove_good_parend_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_comments', to='comment.comment')),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_goods', to='good.good')),
            ],
        ),
        migrations.CreateModel(
            name='GoodTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets_goods', to='good.good')),
                ('tweet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_tweets', to='tweet.tweet')),
            ],
        ),
        migrations.DeleteModel(
            name='GoodParent',
        ),
    ]
