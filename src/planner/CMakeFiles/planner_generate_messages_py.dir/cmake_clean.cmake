FILE(REMOVE_RECURSE
  "CMakeFiles/planner_generate_messages_py"
  "../devel/lib/python2.7/dist-packages/planner/msg/_drone_command.py"
  "../devel/lib/python2.7/dist-packages/planner/msg/__init__.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/planner_generate_messages_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
