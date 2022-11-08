# Create function to represent the file path and the no of bots to be exported
def export (file_path, num_bots):
    print("Exporting....")
    # open file for exporting
    with open (file_path,"a") as csv_file:
        # loop through bots csv file
        for count in range(num_bots):
            print("Please enter the bot id:")
            bot_id = int(input())

            print("Please enter the bot name:")
            bot_name = input()

            print("Please enter the bot paint")
            bot_paint = input()

            data = f"{bot_id},{bot_name},{bot_paint}\n"
            csv_file.write(data)
        print("Done!")"Added code to export csv data."

def run():
    export("exported_bots.csv", 2)

if __name__=="__main__":
    run()


