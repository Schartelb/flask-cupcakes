"""Flask app for Cupcakes"""
from flask import Flask, render_template, flash, redirect, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)


def jsonify_cupcake(cupcake):
    return {"id": cupcake.id,
            "flavor": cupcake.flavor,
            "size": cupcake.size,
            "rating": cupcake.rating,
            "image": cupcake.image}


@app.route("/api/cupcakes", methods=["GET"])
def list_cupcakes():
    """List all cupcakes"""
    cupcakes = Cupcake.query.all()
    return render_template("home.html", cupcakes=cupcakes)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create new Cupcake"""
    new_cupcake = Cupcake(flavor=request.json["flavor"],
                          size=request.json["size"],
                          rating=request.json["rating"],
                          image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=jsonify_cupcake(new_cupcake))
    return (response_json, 201)


@app.route("/api/cupcakes/<int:id>", methods=["GET"])
def single_cupcake(id):
    """Display single cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=jsonify_cupcake(cupcake))


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def single_cupcake_update(id):
    """Update single cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    if cupcake:
        cupcake.flavor = request.json.get("flavor"),
        cupcake.size = request.json.get("size"),
        cupcake.rating = request.json.get("rating"),
        cupcake.image = request.json.get("image")
        db.session.commit()
        return jsonify(cupcake=jsonify_cupcake(cupcake))
    return redirect(f"/api/cupcakes/{id}")  # add error path/catch


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def single_cupcake_delete(id):
    """Delete single cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(msg="Cupcake Deleted")
