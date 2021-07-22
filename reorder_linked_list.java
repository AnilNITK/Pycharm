package newproject;
import java.util.*;

public class reverse_pair {
	node head;
	   
	   static class node{
		   
		   int data;
		   node next;
		   node(int data){
			  this.data=data;
			  next=null;
			  
		}
	 }
	public void display() {
		
		node current=head;
		while(current!=null) {
			System.out.print(current.data+" ---->");
			current=current.next;

	}System.out.println();
		}
	public void atfirst(int value) {
		node newnode=new node(value);
		if(head==null) {
			head=newnode;
		}
		else {
			newnode.next=head;
			head=newnode;
			
		}
		
	}
	public void atend(int value) {
		node newnode=new node(value);
		if(head==null) {
			head=newnode;
		}
		else {
			node current=head;
			while(current.next!=null) {
				current=current.next;
			}
		current.next=newnode;
		}
		
	}
	public void reverse() {
		head = reverse( head);
	}
	public node  reverse(node current) {
		if(current==null) {
			return current;
		}
		node next=current.next;
		if(next==null) {
			
			return current;
		}
		node newnode =reverse(next);
	
		next.next=current;
		current.next=null;
		return newnode;
	}
	public void reversed() {
		reversed(head);
	}
	public void reversed(node head){
		if(head==null) {
			return;
		}
		node slow=head;
		node fast=head.next;
		while(fast!=null && fast.next!=null) {
			slow=slow.next;
			fast=fast.next.next;
		}
		node head1=slow.next;
		slow.next=null;
		Stack<node> stack=new Stack<node>();
		while(head1!=null) {
			node temp=head1;
			head1=head1.next;
			temp.next=null;
			stack.push(temp);
			
		}
		node current= head;
		while(!stack.isEmpty()) {
			node temp1=stack.pop();
			temp1.next=current.next;
			current.next=temp1;
			current=temp1.next;
		}
		
		
	}

public static void main(String arg[]) {
	reverse_pair s11=new reverse_pair();
	s11.head=new node(13);
	node newnode2=new node(12);
	node newnode3=new node(178);
	node newnode4=new node(18);
	node newnode5=new node(5);
	
	s11.head.next=newnode2;
	newnode2.next=newnode3;
	newnode3.next=newnode4;
	newnode4.next=newnode5;
	s11.atfirst(11);
	s11.atend(100);
	
	//s11.reverse();
	
	s11.display();
	s11.reversed();
	s11.display();
	
	}


}



