from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration - replace YOUR_PASSWORD with your actual postgres password
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Rinisha102@localhost:5432/food_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ── MODELS ──────────────────────────────────────────

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.String(20))  # donor, buyer, ngo
    city = db.Column(db.String(50))
    points = db.Column(db.Integer, default=0)

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(20))
    price = db.Column(db.Float, default=0)
    is_free = db.Column(db.Boolean, default=False)
    donor_name = db.Column(db.String(100))
    city = db.Column(db.String(50))

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    food_name = db.Column(db.String(100), nullable=False)
    servings = db.Column(db.Integer)
    ngo_name = db.Column(db.String(100))
    status = db.Column(db.String(20), default='pending')  # pending, accepted, declined, delivered
    city = db.Column(db.String(50))

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    food_name = db.Column(db.String(100), nullable=False)
    restaurant = db.Column(db.String(100))
    price_paid = db.Column(db.Float, default=0)
    money_saved = db.Column(db.Float, default=0)
    points_earned = db.Column(db.Integer, default=0)
    is_free = db.Column(db.Boolean, default=False)

# ── ROUTES ──────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

# ── RUN ─────────────────────────────────────────────

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ All tables created successfully!")
    app.run(debug=True, host='0.0.0.0', port=5000)