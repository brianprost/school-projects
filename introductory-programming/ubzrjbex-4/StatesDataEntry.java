/*
 * StatesDataEntry.java
 * Brian Prost
 * Homework 4
 * 05 July 2020
 */

public class StatesDataEntry {
    // variable declarations
    private String state;
    private String bird;
    private String flower;
    public static String[][] stateInfo = new String[][] { // hold all state names
            { "Alabama", "Yellowhammer", "Camelia" },
            { "Alaska", "Willow Ptarmigan", "Forget-Me-Not" },
            { "Arizona", "Cactus Wren", "Saguaro Cactus Blossom" },
            { "Arkansas", "Mockingbird", "Apple Blossom" },
            { "California", "California Valley Quail", "Golden Poppy" },
            { "Colorado", "Lark Bunting", "Rocky Mountain Columbine" },
            { "Connecticut", "Robin", "Mountain Laurel" },
            { "Delaware", "Blue Hen Chicken", "Peach Blossom" },
            { "Florida", "Mockingbird", "Orange Blossom" },
            { "Georgia", "Brown Thrasher", "Cherokee Rose" },
            { "Hawaii", "Nene", "Hawaiian Hibiscus" },
            { "Idaho", "Mountain Bluebird", "Syringa, mock orange" },
            { "Illinois", "Cardinal", "Violet" },
            { "Indiana", "Cardinal", "Peony" },
            { "Iowa", "Eastern Goldfinch", "Wild Praire Rose" },
            { "Kansas", "Western Meadowlark", "Sunflower" },
            { "Kentucky", "Cardinal", "Goldenrod" },
            { "Louisiana", "Eastern Brown Pelican", "Magnolia" },
            { "Maine", "Chickadee", "Pine Cone and Tassel" },
            { "Maryland", "Baltimore Oriole", "Black-Eyed Susan" },
            { "Massachusetts", "Chickadee", "Mayflower" },
            { "Michigan", "Robin", "Apple Blossom" },
            { "Minnesota", "Common Loon", "Pink and White Lady's Slippper" },
            { "Mississippi", "Mockingbird", "Magnolia" },
            { "Missouri", "Bluebird", "Hawthorn" },
            { "Montana", "Western Meadowlark", "Bitterroot" },
            { "Nebraska", "Western Meadowlark", "Goldenrod" },
            { "Nevada", "Mountain Bluebird", "Sagebrush" },
            { "New Hampshire", "Purple Finch", "Purple Lilac" },
            { "New Jersey", "Eastern Goldfinch", "Violet" },
            { "New Mexico", "Roadrunner", "Yucca Flower" },
            { "New York", "Bluebird", "Rose" },
            { "North Carolina", "Cardinal", "Flowering Dogwood" },
            { "North Dakota", "Western Meadowlark", "Wild Praire Rose" },
            { "Ohio", "Cardinal", "Scarlet Carnation" },
            { "Oklahoma", "Scissor-tailed Flycatcher", "Oklahoma Rose" },
            { "Oregon", "Western Meadowlark", "Oregon Grape" },
            { "Pennsylvania", "Ruffed Grouse", "Mountain Laurel" },
            { "Rhode Island", "Rhode Island Red", "Violet" },
            { "South Carolina", "Great Carolina Wren", "Yellow Jessamine" },
            { "South Dakota", "Ring-necked Pheasant", "Pasque Flower" },
            { "Tennessee", "Mockingbird", "Purple Passionflower" },
            { "Texas", "Mockingbird", "Bluebonnet Sp." },
            { "Utah", "Common American Gull", "Sego Lily" },
            { "Vermont", "Hermit Thrush", "Red Clover" },
            { "Virginia", "Cardinal", " American Dogwood" },
            { "Washington", "Willow Goldfinch", "Coast Rhododendrum" },
            { "West Virginia", "Cardinal", "Rhododendron" },
            { "Wisconsin", "Robin", "Wood Violet" },
            { "Wyoming", "Western Meadowlark", "Indian Paintbrush" }
    };

    // constructor
    public StatesDataEntry(String state, String bird, String flower) {
        this.state = state;
        this.bird = bird;
        this.flower = flower;
    }

    // default constructor
    public StatesDataEntry() {
        // let Washington, DC in on the action
        this.state = "District of Columbia";
        this.bird = "Wood thrush";
        this.flower = "Rosa 'American Beauty'";
    }

    // getters and setters for each variable
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getBird() {
        return bird;
    }

    public void setBird(String bird) {
        this.bird = bird;
    }

    public String getFlower() {
        return flower;
    }

    public void setFlower(String flower) {
        this.flower = flower;
    }

    // to search array for state info
    public static int getInfo(String stateInfo[][], String state) {
        int position = -1;
        boolean found = false;
        for (int index = 0; index < stateInfo.length && !found; index++) {
            if (stateInfo[index][0].equalsIgnoreCase(state)) {
                position = index;
            }
        }
        return position;
    }

    public static String[] findStateData(String stateEntered, String[][] stateInfo) {
        String[] stateData = null; // initialize 1d array
        for (int i = 0; i < stateInfo.length; i++) {
            if (stateInfo[i][0].equalsIgnoreCase(stateEntered)) {
                stateData = new String[3]; // will store data from stateInfo in a 1d array
                for (int j = 1; j < stateInfo[i].length; j++) {
                    stateData[j - 1] = stateInfo[i][j]; // stores data here
                }
                break;
            }
        }
        return stateData;
    }

    // print info
    public String printInfo(String state, String stateBird, String stateFlower) {
        String printMe = ("State: " + state + "\tBird: " + stateBird + "\tFlower: " + stateFlower);
        return printMe;
    }
}