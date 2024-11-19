from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from models import db, Todo

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration Swagger
api = Api(app, version='1.0', title='Todo List API', description='Une API pour gérer des tâches')
ns = api.namespace('tasks', description='Opérations sur les tâches')

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Modèle de données pour Swagger (description de la tâche)
task_model = api.model('Task', {
    'id': fields.Integer(required=True, description="L'identifiant de la tâche", example=1),
    'title': fields.String(required=True, description="Le titre de la tâche", example="Acheter du lait"),
    'done': fields.Boolean(required=True, description="Statut de la tâche", example=False)
})

# Route pour récupérer toutes les tâches
@ns.route('/')
class TaskList(Resource):
    @api.doc('get_tasks')
    @api.response(200, 'Liste des tâches récupérée avec succès')
    def get(self):
        """Obtenir toutes les tâches"""
        tasks = Todo.query.all()
        return jsonify([task.to_dict() for task in tasks])

    @api.expect(task_model)  # Spécifie le modèle attendu pour la requête POST
    @api.response(201, 'Tâche ajoutée avec succès')
    @api.response(400, 'Données invalides')
    def post(self):
        """Ajouter une nouvelle tâche"""
        data = request.get_json()
        new_task = Todo(title=data['title'], done=False)
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201

# Route pour récupérer, modifier ou supprimer une tâche par ID
@ns.route('/<int:id>')
@api.response(404, 'Tâche non trouvée')
class Task(Resource):
    @api.doc('get_task')
    @api.response(200, 'Tâche récupérée avec succès')
    def get(self, id):
        """Récupérer une tâche spécifique"""
        task = Todo.query.get_or_404(id)
        return jsonify(task.to_dict())

    @api.expect(task_model)  # Spécifie le modèle attendu pour la requête PUT
    @api.response(200, 'Tâche modifiée avec succès')
    def put(self, id):
        """Modifier une tâche existante"""
        task = Todo.query.get_or_404(id)
        data = request.get_json()
        task.title = data.get('title', task.title)
        task.done = data.get('done', task.done)
        db.session.commit()
        return jsonify(task.to_dict())

    @api.response(200, 'Tâche supprimée avec succès')
    def delete(self, id):
        """Supprimer une tâche"""
        task = Todo.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
