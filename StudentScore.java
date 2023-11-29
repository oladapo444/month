import java.utill.scanner;

  public class StudentScore  {

  public static vold main(String [ ] arg){

 Scanner scanner = new scanner(System.in);
 System.out.print("Enter Student score");
 int  numberOfStudent = input . nextint();
      highest score = 0;
      secondhighest = 0;
 System.out.print("Enter Student score");
  int  numberOfStudent = input . nextint();
   
for (int i = 0; i < numberOfStudents; i++) {
			System.out.print(
				"Student: " + (i + 1) + "\n   Name: ");
			name = input.next();
			System.out.print("   Score: ");
			score = input.nextInt();

			if (i == 0) {

if (i == 0) {
			
				highest = score;
				student1 = name;
			}
			else if (i == 1 && score > highest) {
				// Second student entered scored
				// higher than first student
				secondHigest = highest;
				highest = score;
				student2 = student1;
				student1 = name;
			}
			else if (i == 1) {
				// Second student entered scored
				// lower than first student
				secondHigest = score;
				student2 = name;
			}		
			else if (i > 1 && score > highest && score > secondHigest) {
				// Last student entered has the highest score 
				secondHigest = highest;
				student2 = student1;
				highest = score;
				student1 = name;
			}
			else if (i > 1 && score > secondHigest) {
				// Last student entered has the second highest score 
				student2 = name;
				secondHigest = score;
			       }
		}

	