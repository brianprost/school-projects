/*
* Brian Prost
* Project4.java
* Main method & GUI
* 14 November 2020
* */

package ubzrjbexSbhe;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.TreeMap;

public class Project4 extends JFrame {

    // transaction
    static JLabel transactionNumberLabel = new JLabel("Transaction #:");
    static JTextField transactionNumberField = new JTextField();

    // address
    static JLabel addressLabel = new JLabel("Address:");
    static JTextField addressField = new JTextField();

    // number of bedrooms
    static JLabel numberOfBedroomsLabel = new JLabel("Bedrooms:");
    static JTextField numberOfBedroomsField = new JTextField();

    // square footage
    static JLabel squareFeetLabel = new JLabel("Square Footage:");
    static JTextField squareFeetField = new JTextField();

    // property price
    static JLabel priceLabel = new JLabel("Price:");
    static JTextField priceField = new JTextField();

    // process button
    static JButton processButton = new JButton("Process");

    // database operations
    static String[] databaseOperations = { "Insert", "Delete", "Find" };
    static JComboBox databaseOperationsChooser = new JComboBox(databaseOperations);

    // change status operations
    static JButton changeStatusButton = new JButton("Change Status");
    static Status[] changeStatusOptions = { Status.FOR_SALE, Status.UNDER_CONTRACT, Status.SOLD };
    static JComboBox changeStatusChooser = new JComboBox(changeStatusOptions);

    // tree map as a database. they key will be the transaction number and Property
    // object as value
    TreeMap<Integer, Property> propertyRecords = new TreeMap<>();

    public Project4() {
        // set up frame
        super("Real Estate Database");
        setSize(387, 297);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new FlowLayout());

        // setup userInputPanel
        JPanel userInputPanel = new JPanel();
        userInputPanel.setLayout(new GridLayout(7, 2, 10, 2));

        // add elements to userInputPanel.
        // ...this cannot be the most efficient way to do the following
        userInputPanel.add(transactionNumberLabel);
        userInputPanel.add(transactionNumberField);
        userInputPanel.add(addressLabel);
        userInputPanel.add(addressField);
        userInputPanel.add(numberOfBedroomsLabel);
        userInputPanel.add(numberOfBedroomsField);
        userInputPanel.add(squareFeetLabel);
        userInputPanel.add(squareFeetField);
        userInputPanel.add(priceLabel);
        userInputPanel.add(priceField);
        processButton.addActionListener(new processButtonClick());
        userInputPanel.add(processButton);
        userInputPanel.add(databaseOperationsChooser);
        changeStatusButton.addActionListener(new changeStatusButtonClick());
        userInputPanel.add(changeStatusButton);
        userInputPanel.add(changeStatusChooser);
        // add panel to Frame
        add(userInputPanel);
    }

    // define action when user clicks on the process button. gosh i'm good at naming
    // button listeners
    private class processButtonClick implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            int databaseActionChoice = databaseOperationsChooser.getSelectedIndex();
            try {
                switch (databaseActionChoice) {
                    // insert
                    case 0 -> {
                        // see if it already exists in records
                        checkForDuplicateRecord(Integer.parseInt(transactionNumberField.getText()));
                        // add it
                        propertyRecords.put(Integer.parseInt(transactionNumberField.getText()), getPropertyInfo());
                        // confirm addition
                        JOptionPane.showMessageDialog(null, "Entry added to database.");
                    }
                    // delete
                    case 1 -> {
                        // make sure record actually exists before deleting record
                        checkForExistingRecord(Integer.parseInt(transactionNumberField.getText()));
                        // delete it
                        propertyRecords.remove(Integer.parseInt(transactionNumberField.getText()));
                        // confirm removal
                        JOptionPane.showMessageDialog(null, "Entry removed from database.");
                    }
                    // find
                    case 2 -> {
                        // make sure record actually exists before bringing up info
                        checkForExistingRecord(Integer.parseInt(transactionNumberField.getText()));
                        // add property to memory. I think it's putting it in memory? Regardless, it's
                        // bring it up
                        // it's grabbing it by the transaction key
                        Property propertyToFind = propertyRecords
                                .get(Integer.parseInt(transactionNumberField.getText()));
                        // popup to display info
                        JOptionPane.showMessageDialog(null, propertyToFind.toString());
                    }
                }
            } catch (NumberFormatException numberFormatException) {
                JOptionPane.showMessageDialog(null, "Please enter data in correct format.");
            } catch (DuplicatePropertyException duplicatePropertyException) {
                JOptionPane.showMessageDialog(null, "Entry already exists.");
            } catch (PropertyNotFoundException propertyNotFoundException) {
                JOptionPane.showMessageDialog(null, "Entry not found.");
            }
        }
    }

    // action when change status button is clicked
    private class changeStatusButtonClick implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            try {
                // grab status selection index
                Status statusChoice = (Status) changeStatusChooser.getSelectedItem();
                // verify it's actually in the record books
                checkForExistingRecord(Integer.parseInt(transactionNumberField.getText()));
                // change the property
                Property propertyToBeChanged = propertyRecords.get(Integer.parseInt(transactionNumberField.getText()));
                propertyToBeChanged.changeState(statusChoice);
                propertyRecords.put(Integer.parseInt(transactionNumberField.getText()), propertyToBeChanged);
                // pop up and confirm status change
                JOptionPane.showMessageDialog(null, "Status changed.");
            } catch (PropertyNotFoundException propertyNotFoundException) {
                JOptionPane.showMessageDialog(null, "Not found in the records.");
            } catch (NumberFormatException numberFormatException) {
                JOptionPane.showMessageDialog(null, "Please use appropriate values.");
            }
        }
    }

    // method that returns a constructed Property object from user input
    private Property getPropertyInfo() {
        return new Property(
                /*
                 * sorry to put another question in here, but I keep getting tool-tips from my
                 * IDE
                 * that getText() is deprecated. Is there another way to grab the text?
                 */
                addressField.getText(),
                Integer.parseInt(numberOfBedroomsField.getText()),
                Integer.parseInt(squareFeetField.getText()),
                Integer.parseInt(priceField.getText()));
    }

    // checks if entry is already in the records and throws
    // DuplicatePropertyException if so
    private void checkForDuplicateRecord(int transactionNumberField) throws DuplicatePropertyException {
        if (propertyRecords.containsKey(transactionNumberField)) {
            throw new DuplicatePropertyException();
        }
    }

    // checks if entry is not already in the records and throws
    // PropertyNotFoundException if so
    private void checkForExistingRecord(int transactionKey) throws PropertyNotFoundException {
        if (!propertyRecords.containsKey(transactionKey)) {
            throw new PropertyNotFoundException();
        }
    }

    // define custom exception for no results
    private static class PropertyNotFoundException extends Exception {
        public PropertyNotFoundException() {
            super();
        }
    }

    // defines custom exception for duplicate entry
    private static class DuplicatePropertyException extends Exception {
        public DuplicatePropertyException() {
            super();
        }
    }

    public static void main(String[] args) {
        try {
            new Project4().setVisible(true);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}