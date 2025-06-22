class Summary:
    def __init__(self, id, student, status, made_a_difference, covered_value, recommendation, gender):
        self.id = id
        self.student = student
        self.status = status
        self.made_a_difference = made_a_difference
        self.covered_value = covered_value
        self.recommendation = recommendation
        self.gender = gender

    # unlike java, python does support multiple constructors
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            student=data.get('student'),
            status=data.get('status'),
            made_a_difference=data.get('made_a_difference'),
            covered_value=data.get('covered_value'),
            recommendation=data.get('recommendation'),
            gender=data.get('gender')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'student': self.student,
            'status': self.status,
            'made_a_difference': self.made_a_difference,
            'covered_value': self.covered_value,
            'recommendation': self.recommendation,
            'gender': self.gender
        }

    def __str__(self):
        return (
            f"Summary(id={self.id}, student={self.student}, status={self.status}, "
            f"made_a_difference={self.made_a_difference}, covered_value={self.covered_value}, "
            f"recommendation={self.recommendation}, gender={self.gender})"
        )