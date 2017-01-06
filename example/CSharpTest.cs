using System;
namespace CSharpTest{
	public class Person{
		private string name;
		private bool sex;
		private string birthday;
		public Person{}
		public Person(string newName,bool newSex,string newBirthday){
			this.name = newName;
			this.sex = newSex;
			this.birthday = newBirthday;
		}
		public string Name{
			get{
				return name;
			}
			set{
				name = value;
			}
		}
		public bool Sex{
			get{
				return sex;
			}
			set{
				sex = value;
			}
		}
		public string Birthday{
			get{
				return birthday;
			}
			set{
				birthday = value;
			}
		}
		public virtual void introduction(string name,bool sex){
			Console.WriteLine("I'm {0} and {1}",name,sex?male:female);

		}
	}
	public class Student:Person{
		private int score;
		public int Score{
			get{
				return score;
			}
			set{
				score = value;
			}
		}
		private string course;
		public new void introduction(string name,bool sex){
			Console.WriteLine("I'm Student {0} and {1}",name,sex?male:female);
		}
	}
	public class Teacher:Person{
		private int classNum;
		public override introduction(string name,bool sex){
			Console.WriteLine("I'm Teacher {0} and {1}",name,sex?male:female);
		}
	}
	static void Main(){
		string[] names = {"A","B","C","D","E"};
		bool[] sexs = {false,true,false,true,true};
		var query = from i in Enumerable.Range(0,5)
					select new Person(names[i],sexs[i],"1990-01-01");
		Console.WriteLine("Enter a number:");
		int num = int.Parse(Console.ReadLine());
		Person p = new Person();
		p.setName("Kai");
		p.setSex(true);
		p.introduction();
		Console.ReadKey();
	}


}

namespace OverrideAndNew{
	class Car{
		public void DescribeCar(){
			Console.WriteLine("Four wheels and an engine.");
			ShowDetails();
		}
		public virtual void ShowDetails(){
			Console.WriteLine("Standard transportation.");
		}
	}
	class ConvertibleCar : Car{
		public new void ShowDetails(){
			Console.WriteLine("A roof that opens up.");
		}
	}
	class Minicvan : Car{
		public override void ShowDetails(){
			Console.WriteLine("Carries seven people.");
		}
	}

	static void Main(string[] args){
		Console.WriteLine("");
	}
}