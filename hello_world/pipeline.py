import sematic

@sematic.func
def hello_world() -> str:
  return "Hello world"

@sematic.func
def my_name_is(name: str) -> str:
  return "my name is {}".format(name)

@sematic.func
def nice_to_meet_you(hello: str, name_is: str) -> str:
  return "{}, {}. Nice to meet you.".format(hello, name_is)

@sematic.func
def pipeline(name: str) -> str:
  """
  My very first hello-world Sematic pipeline.
  """
  hellow = hello_world()
  name_is = my_name_is(name)
  return nice_to_meet_you(hellow, name_is)
