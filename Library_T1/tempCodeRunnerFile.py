for text, cmd in buttons:
    tk.Button(btn_frame, text=text, command=cmd, font=("Arial", 12), width=20, bg="#f4a261", fg="white").pack(pady=5)

# Output Area
output_area = tk.Text(root, height=15, width=80, font=("Courier", 10))
output_area.pack(pady=10)

root.mainloop()