def askUserName() -> str:
  name = input("What is your name?\n")
  return name

def greetUser(user: str) -> None:
  print(f'Hello, {user}')

if __name__ == "__main__":
  print("Hello, world!")
  user_name = askUserName()
  greetUser(user_name)