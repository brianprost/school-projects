/*
* Brian Prost
* StateChangeable.java
* generic interface defining one abstract method changeState()
* 14 November 2020
* */

package homeworkSbhe;

public interface StateChangeable<T extends Enum<T>> {
    abstract void changeState(T t);
}
