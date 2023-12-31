#!/usr/bin/python3

""" Base module that contains the Base class which will be the
“base” of all other classes in the project.
"""

import turtle
import json
import csv

class Base:
    """ Base class to manage id attribute in all future classes """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            # increment __nb_objects & assign the new value to the id attribute
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to return JSON string representation - list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation into a file.
        Args:
            cls (class): The class (e.g., Rectagle, Square, etc).
            list_objs (list of instances): instances that inherits from Base.
        """
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(cls.to_dictionary(obj))

        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'w') as my_file:
            my_file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.
        Args:
            json_string (str): JSON string representing a list of dictionaries.
        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set using the provided dictionary.
        Args:
            cls (class): The class (e.g., Rectangle or Square).
            **dictionary: A dictionary containing attribute-value pairs.
        Returns:
            Base: An instance of the class with attributes set
            based on the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            inert = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == 'Square':
            inert = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Unsupported class")
        # Use the update method to apply attributes from the dictionary
        inert.update(**dictionary)
        return inert

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file.
        Returns:
            list: A list of instances.
        """
        filename = '{}.json'.format(cls.__name__)
        instance_list = []

        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                data_list = cls.from_json_string(json_data)
                for data in data_list:
                    instance = cls.create(**data)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list of instances to a CSV file.
        Args:
            cls (class): the class (Rectangle, Square, etc)
            list_objs (list of instances) : list of instances to be serialized.
        """
        filename = '{}.csv'.format(cls.__name__)
        with open(filename, 'w', newline='') as my_file:
            writer = csv.writer(my_file)
            for x in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([x.id, x.width, x.height, x.x, x.y])
                if cls.__name__ == "Square":
                    writer.writerow([x.id, x.size, x.x, x.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file.
        Returns:
            list: list of instances.
        """
        instance_list = []
        filename = '{}.csv'.format(cls.__name__)

        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    data = {"id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])}
                if cls.__name__ == "Square":
                    data = {"id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])}
                instance = cls.create(**data)
                instance_list.append(instance)
        return instance_list

# Turtle Graphics module task
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the Turtle graphics module.
        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.
        Returns:
            None
        """
        # Create a Turtle screen
        window = turtle.Screen()
        window.bgcolor("white")

        # Create Turtle object
        pen = turtle.Turtle()
        pen.speed(2)

        # Draw rectangles
        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            for x in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        # Draw Squares
        for s_box in list_squares:
            pen.penup()
            pen.goto(s_box.x, s_box.y)
            pen.pendown()
            pen.color("red")
            for y in range(4):
                pen.forward(s_box.size)
                pen.left(90)

        # close Turtle graphics window when clicked.
        window.exitonclick()
