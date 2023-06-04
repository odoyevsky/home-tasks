import scala.annotation.tailrec

/**
 * Есть список из интов. Подсчитать количество перемен знака в последовательности (ноль не перемена)
 * Для List(0, 0, 1, 0, 0, 1, 0, 1) - 0 перемен знака
 * Для List(1, 0 , -1)              - 1 перемена
 * Для List(1, 0 , -1, 0, 0, 0, -1) - тоже 1 перемена
 * Желательно сделать на Scala, но можно и на другом языке обязательно в функциональном стиле: использовать чистые функции, не использовать циклы, переменные.
 * Как вариант можно сделать задание, используя хвостовую рекурсию, но можно и другим способом
 */

object PositiveNegativeCount extends App {
  def countSignChanges(list: List[Int]): Int = {
    @tailrec
    def calculateSignChangeCount(list: List[Int], previousNumber: Option[Int], count: Int): Int = {
      list match {
        case Nil => count
        case head :: tail =>
          val prevNumber = previousNumber match {
            case Some(previousNumber) if (head == 0) => previousNumber
            case _ => head
          }

          val newCount = previousNumber match {
            case Some(previousNumber) if head * previousNumber < 0 => count + 1
            case _ => count
          }

          calculateSignChangeCount(tail, Some(prevNumber), newCount)
      }
    }

    calculateSignChangeCount(list, None, 0)
  }


  val List1 = List(0, 0, 1, 0, 0, 1, 0, 1) // 0
  val List2 = List(1, 0, -1) // 1
  val List3 = List(1, 0, -1, 0, 0, 0, -1) // 1
  val List4 = List(1, -2, 3, 3, 4, -2, -2, -3, 1) // 4
  val List5 = List(0) // 0
  val List6 = List() // 0
  val List7 = List(0, 0, 0, -1, 0, -99, 1, 2, 4, 0, -777, 0) // 2
  val List8 = List(0, -1, 0, -99, 1, -2, 4, 0, 0, 1) // 3

  assert(countSignChanges(List1) == 0)
  assert(countSignChanges(List2) == 1)
  assert(countSignChanges(List3) == 1)
  assert(countSignChanges(List4) == 4)
  assert(countSignChanges(List5) == 0)
  assert(countSignChanges(List6) == 0)
  assert(countSignChanges(List7) == 2)
  assert(countSignChanges(List8) == 3)
}
