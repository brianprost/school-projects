/*
TestStatesData.java
Brian Prost
Homework 4
07 July 2020
 */

import java.util.Scanner; // scanner class

public class TestStatesData {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 0; // variable for storing state names in array and for iteration through while
                   // loop
        String[] stateEnteredDb = new String[50];

        String[] allStateInfo = new String[StatesDataEntry.stateInfo.length]; // holds all state info that we will call

        while (true) { // so that we can run until none is entered
            System.out.println("Enter a state:");
            String stateEntered = sc.next();
            switch (stateEntered) { // goes to default case unless "none" is entered
                case "none":
                    System.out.println("\n****ROUND UP:****");
                    for (int i = 0; i < a; i++) { // print state info
                        System.out.println("State: " + allStateInfo[i]);
                    }
                    System.out.println("\nGOODBYE!");
                    System.exit(0); // exit
                default:
                    stateEnteredDb[a] = stateEntered; // stores each state entered
                    String[] stateData = (StatesDataEntry.findStateData(stateEntered, StatesDataEntry.stateInfo)); // calls
                                                                                                                   // findStateData
                                                                                                                   // and
                                                                                                                   // stores
                                                                                                                   // it
                                                                                                                   // in
                                                                                                                   // stateData
                                                                                                                   // array
                    // construct class
                    StatesDataEntry stateSelected = new StatesDataEntry(stateEntered, stateData[0], stateData[1]);
                    // gets
                    String stateName = stateSelected.getState();
                    String stateBird = stateSelected.getBird();
                    String stateFlower = stateSelected.getFlower();
                    // print info about each state and save it in an array so we can call it again
                    // at the end
                    allStateInfo[a] = stateSelected.printInfo(stateEntered, stateBird, stateFlower);
                    // print it out
                    System.out.println(allStateInfo[a]);
                    // iterate
                    a++;
            }
        }
    }

}
