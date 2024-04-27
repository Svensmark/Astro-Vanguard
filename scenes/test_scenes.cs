using Godot;
using System;

public partial class test_scenes : Control
{
	// Called when the node enters the scene tree for the first time

	public override void _Ready()
	{ 
		Button start_button = GetNode<Button>("MarginContainer/HBoxContainer/VBoxContainer/Start Button");
		Button exit_button = GetNode<Button>("MarginContainer/HBoxContainer/VBoxContainer/Exit Button");
		
		start_button.Pressed += StartButton_Pressed;
		exit_button.Pressed += ExitButton_Pressed;
	}
	
	private void StartButton_Pressed()
	{
		GD.Print("Start button clicked!");
	}

	private void ExitButton_Pressed()
	{
		GetTree().Quit();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}
