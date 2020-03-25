def validBraces(string):
  BRACKETS_MAP = {"[": "]", "{": "}", "(": ")"}
  stack = []
  for b in string:
      if b in BRACKETS_MAP:
          stack.append(BRACKETS_MAP[b])
      elif not stack or b != stack.pop():
          return False
  return not stack