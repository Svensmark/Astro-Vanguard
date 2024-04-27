using Godot;
using System;

public partial class Player : Area2D
{
	[Export]
	public int Speed { get; set; } = 400;
	[Export]
	public int Acceleration { get; set; } = 40;
	[Export]
	public int MaxSpeed { get; set; } = 400;
	[Export]
	public double Friction  { get; set; } = .15;
	public Vector2 ScreenSize;
	
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		ScreenSize = GetViewportRect().Size;
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Vector2 inputDirection = Input.GetVector("move_left", "move_right", "move_up", "move_down");

		if (inputDirection.Length() > 0)
		{
			inputDirection = inputDirection.Normalized() * Speed;
		}
	}
}
