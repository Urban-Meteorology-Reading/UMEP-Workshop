.. _BEG1:

Metrics for Model evaluation
----------------------------

Methods commonly used to evaluate model performance, include:

* Mean absolute error (MAE)

.. math::

    \mathrm{MAE}=\frac{1}{N} \sum_{i=1}^{N}\left|y_{i}-\hat{y}_{i}\right|

where :math:`N` is number of observations, :math:`y_i` the actual expected output
and :math:`\hat{y}_{i}` the model’s prediction
(same notations below if not indicated otherwise).

* Mean bias error (MBE)

.. math::

    \mathrm{MBE}=\frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\hat{y}_{i}\right)

* Mean square error (MSE)

.. math::

    \mathrm{MSE}=\frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\hat{y}_{i}\right)^{2}


* Root mean square error (RMSE)

.. math::

    \mathrm{RMSE}=\sqrt{\frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\hat{y}_{i}\right)^{2}}


* Coefficient of determination (:math:`R^2`)

.. math::

    R^{2}=
    1-\frac{\mathrm{MSE}(\text { model })}
    {\mathrm{MSE}(\text { baseline })}

    \mathrm{MSE}(\text { baseline })=
    \frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\overline{y}\right)^{2}

where :math:`\overline{y}` is mean of observed :math:`y_i`.


Combined with plots (e.g. scatter, time series) allows identification of periods
when a model performs well/poorly relative to observations.
It should be remembered that both the model (e.g. parameters, forcing data)
and the evaluation observations have errors.
