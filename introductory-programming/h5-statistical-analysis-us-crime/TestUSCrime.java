/*
TestUSCrime.java
Brian Prost
13 July 2020
This tests the USCrime class
 */

// library imports
import java.io.IOException;
import java.util.Scanner;

public class TestUSCrime {
    public static void main(String[] args) throws IOException, InterruptedException {
        // define CrimeFileReader class and call
        long stopWatchTime = System.currentTimeMillis();
        CrimeFileReader fileReader = new CrimeFileReader();
        fileReader.Open(args[0]); // args[0] is the filepath of the file
        doMenu(); // prints the menu. I guess this could've been in the main function but trying
                  // to practice modularity
        long elapsedTime = ((System.currentTimeMillis() - stopWatchTime) / 1000);
        System.out.printf("Thanks for reading our data. You've been using this program for %d seconds." +
                "Hope it was worth your time!", elapsedTime);
    }

    private static void doMenu() throws InterruptedException {
        Scanner sc = new Scanner(System.in); // to read user input
        String menuChoice = "";
        // this will run into the user enters q on the menu
        while (!menuChoice.equals("q")) {
            // two print statments so that we can be pretty
            System.out.println("\n\t\t* * * W E L C O M E * * *" +
                    "\n\t* To the US Crime Statistical Application *" +
                    "\n\nEnter the number of the question you want answered, or press 'Q' to quit.");
            System.out.println(
                    "\n" +
                            "1. What were the percentages in population growth " +
                            "for each consecutive year from 1994 to 2013?" +
                            "\n2. In which year was the murder rate the highest?" +
                            "\n3. In which year was the murder rate the lowest?" +
                            "\n4. In which year was the robbery rate the highest?" +
                            "\n5. In which year was the robbery rate the lowest?" +
                            "\n6. In which year was motor vehicle theft the highest?" +
                            "\n7. In which year was motor vehicle theft the lowest?" +
                            "\nQ. Quit me. (It's not you, it's me, but it's over.)");
            System.out.print("\n\tWhich would you like to do? ");

            // accepts input and converts to lower case
            // just in case user enters a capital Q when they want to quit
            menuChoice = sc.next().toLowerCase().trim();

            // switch statement to call function dependent on user input
            switch (menuChoice) {
                case "1":
                    System.out.println(USCrime.getPercentagePopulationGrowth());
                    break;
                case "2":
                    System.out.printf("The murder rate was the highest in %d\n", USCrime.getHighestMurderRateYear());
                    break;
                case "3":
                    System.out.printf("The murder rate was the lowest in %d\n", USCrime.getLowestMurderRateYear());
                    break;
                case "4":
                    System.out.printf("The robbery rate was the highest in %d\n", USCrime.getHighestRobberyRateYear());
                    break;
                case "5":
                    System.out.printf("The robbery rate was the lowest in %d\n", USCrime.getLowestRobberyRateYear());
                    break;
                case "6":
                    System.out.printf("The year that motor vehicle theft was the highest was %d\n",
                            USCrime.getHighestMotorVehicleTheftYear());
                    break;
                case "7":
                    System.out.printf("The year that motor vehicle theft was the lowest was %d\n",
                            USCrime.getLowestMotorVehicleTheftYear());
                    break;
                case "q":
                    System.out.println("Goodbye!");
                    break;
                default:
                    System.out.print("Invalid input. Try again.");
                    break;
            }
        }
    }
}
