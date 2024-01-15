This repository errors out because of this issue https://github.com/EmilStenstrom/django-components/issues/300

Running `python manage.py compress --force` throws the following error:

```
Compressing... Traceback (most recent call last):
  File "C:\progr\py3\ehcg\components_compress\manage.py", line 22, in <module>
    main()
  File "C:\progr\py3\ehcg\components_compress\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "C:\progr\py3\ehcg\venv\lib\site-packages\django\core\management\__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "C:\progr\py3\ehcg\venv\lib\site-packages\django\core\management\__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "C:\progr\py3\ehcg\venv\lib\site-packages\django\core\management\base.py", line 412, in run_from_argv
    self.execute(*args, **cmd_options)
  File "C:\progr\py3\ehcg\venv\lib\site-packages\django\core\management\base.py", line 458, in execute
    output = self.handle(*args, **options)
  File "C:\progr\py3\ehcg\venv\lib\site-packages\compressor\management\commands\compress.py", line 370, in handle
    self.handle_inner(**options)
  File "C:\progr\py3\ehcg\venv\lib\site-packages\compressor\management\commands\compress.py", line 395, in handle_inner
    offline_manifest, block_count, results = self.compress(
  File "C:\progr\py3\ehcg\venv\lib\site-packages\compressor\management\commands\compress.py", line 257, in compress
    nodes = list(parser.walk_nodes(template, context=context))
  File "C:\progr\py3\ehcg\venv\lib\site-packages\compressor\offline\django.py", line 161, in walk_nodes
    for node in self.walk_nodes(node, original, context):
  File "C:\progr\py3\ehcg\venv\lib\site-packages\compressor\offline\django.py", line 155, in walk_nodes
    for node in self.get_nodelist(node, original, context):
  File "C:\progr\py3\ehcg\venv\lib\site-packages\compressor\offline\django.py", line 135, in get_nodelist
    return handle_extendsnode(node, context)
  File "C:\progr\py3\ehcg\venv\lib\site-packages\compressor\offline\django.py", line 47, in handle_extendsnode
    new_nodelist = remove_block_nodes(parent_nodelist, block_stack, block_context)
  File "C:\progr\py3\ehcg\venv\lib\site-packages\compressor\offline\django.py", line 84, in remove_block_nodes
    setattr(node, attr, sub_nodelist)
AttributeError: can't set attribute 'nodelist'
```

Please notice that you can apply the patch at https://github.com/spapas/django-compressor to catch the exception.
