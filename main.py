# Downloading files from Kaggle (default location: C:\Users\<user name>>\.cache\kagglehub\datasets
# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("muhammadatiflatif/coca-cola-stock-data-over-100-years-of-trading")
#
# print("Path to dataset files:", path)
#######################################################################################################################
import plots
import analysis
import keyboard
import time


def main():
    print("Press [1] to show plots")
    print("Press [2] to show calculations")
    print("Press [Esc] to exit")
    try:
        while True:
            if keyboard.is_pressed('1'):
                print("\nShowing plots")
                plots.all_plots()
                time.sleep(1)
            elif keyboard.is_pressed('2'):
                print("\nPerforming analysis")
                analysis.analise()
                time.sleep(1)
            elif keyboard.is_pressed('esc'):
                print("\nFinished")
                break
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == '__main__':
    main()
