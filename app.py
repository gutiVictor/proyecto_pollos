from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        data = request.get_json()

        # Datos de compra
        precio_pollo_unidad = float(data['precio_pollo_unidad'])
        cantidad_pollos_comprados = float(data['cantidad_pollos_comprados'])
        cantidad_bultos = float(data['cantidad_bultos'])
        valor_bulto = float(data['valor_bulto'])

        # Datos de venta
        cantidad_pollos_vender = float(data['cantidad_pollos_vender'])
        peso_cada_pollo = float(data['peso_cada_pollo'])
        precio_venta_libra = float(data['precio_venta_libra'])

        # Cálculos
        costo_total_pollos = precio_pollo_unidad * cantidad_pollos_comprados
        costo_total_comida = cantidad_bultos * valor_bulto
        inversion_total = costo_total_pollos + costo_total_comida

        ingreso_total = cantidad_pollos_vender * peso_cada_pollo * precio_venta_libra
        ganancia_neta = ingreso_total - inversion_total

        # Inversión por pollo (sobre los comprados)
        if cantidad_pollos_comprados > 0:
            inversion_por_pollo = inversion_total / cantidad_pollos_comprados
        else:
            inversion_por_pollo = 0

        return jsonify({
            'costo_total_pollos': round(costo_total_pollos, 2),
            'costo_total_comida': round(costo_total_comida, 2),
            'inversion_total': round(inversion_total, 2),
            'ingreso_total': round(ingreso_total, 2),
            'ganancia_neta': round(ganancia_neta, 2),
            'inversion_por_pollo': round(inversion_por_pollo, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)