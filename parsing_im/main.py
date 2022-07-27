from parser_class import Parser
def main() -> None:
    parser = Parser()
    try:
        parser.__start_parsing__("https://www.google.ru/")
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()