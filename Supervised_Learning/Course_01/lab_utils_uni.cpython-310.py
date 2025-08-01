o
    ��h�8  �                   @   s  d Z ddlZddlmZ ddlmZ ddlm	Z	 ddl
mZ ddlmZ ddlmZ ddlmZmZmZmZmZmZ ej�d	� d
Zejdeed�Zd)dd�Zdd� Zdd� Zdd� ZG dd� d�Zdd� Z dd� Z!g d�g d�g d�d
ddd fd!d"�Z"d#d$� Z#d%d&� Z$d'd(� Z%dS )*zl 
lab_utils_uni.py
    routines used in Course 1, Week2, labs1-3 dealing with single variables (univariate)
�    N)�MaxNLocator)�GridSpec)�LinearSegmentedColormap)�interact)�compute_cost)�dlblue�dlorange�	dldarkred�	dlmagenta�dlpurple�dlcolorsz./deeplearning.mplstyle�   Zdl_map)�Nc                 C   sl   |s
t �dd�\}}|j| |dddd� |�d� |�d� |�d� |d	ur0|j| |td
d� |��  d	S )z plot house with aXis �   �x�rzActual Value)�marker�c�labelzHousing PriceszPrice (in 1000s of dollars)zSize (1000 sqft)NzOur Prediction)r   r   )	�plt�subplots�scatter�	set_title�
set_ylabel�
set_xlabel�plotr   �legend)�X�y�f_wb�ax�fig� r"   �Dc:\College-Work\AI_ML_Portfolio\Supervised_Learning\lab_utils_uni.py�plt_house_x   s   


r$   c              
   C   s  d}d}d}d}t | |�D ]a}	||	d  | }
|
|	d  d d }|}|j|	d |	d |
dtd|d	� d
}|	d |	d |
|	d  d  g}|j|d�|dtddd� ||d�d�7 }t|�dkrj|du rj|d7 }d}||7 }q|t| � }|dd� d|d�� }|jdd||jtd� dS )z makes vertical cost lineszcost = (1/m)*(r   zcost for pointFr   �   �   �dotted)�lw�color�lsr   � �0.0f�data)r   r   �offset points)�xy�xycoordsr)   �xytext�
textcoordsz +�&   �
TN�����z) = g333333�?g{�G�z�?)�	transformr)   )�zip�vlinesr   �annotate�len�text�	transAxes)r   r   �w�br    ZcstrZctotr   Z
addedbreak�pZf_wb_pZc_pZc_p_txt�cxyr"   r"   r#   �mk_cost_lines%   s,     �
rA   c                    s�   t �ddg�}d�t jg |�d�R � �t ���� tt���D ]}�| }t��|��� |< qtg |�d�R dd�d� ����fd	d
�	�}d S )Nr   �  �d   r   �
   F)r=   Zcontinuous_update�   c                    s<  t ��| �� }tjddddd�\}}d|j_t��| �|d � t��||d d� |d ��� � t	��| ��}|d j
| |d	td
d| � �d� |d j||d �� d | dtdd� |d j| |d �� d |dtdd� |d �d� |d �d� |d �d� |d jdd� |jd|d��dd� t��  d S )Nr   r%   T)�   �   )�constrained_layout�figsize�bottomr   �r   r    rC   rD   z
cost at w=��sr)   �zorderr   rG   r'   �r(   r)   r*   zCost vs. w, (b fixed at 100)�Costr=   zupper center)�loczMinimize Cost: Current Cost = r,   �   ��fontsize)�np�dotr   r   �canvas�toolbar_positionrA   r$   r   r   r   r	   �hlines�get_xlimr   r8   �get_ylimr   r   r   r   �suptitle�show)r=   r   r!   r    Zcur_cost��cost�tmp_b�w_array�x_train�y_trainr"   r#   �funcM   s     &&zplt_intuition.<locals>.func)rE   )rU   �array�arange�
zeros_like�ranger:   r   r   )rb   rc   �w_range�i�tmp_wrd   r"   r^   r#   �plt_intuitionB   s   
rl   c              
   C   sB  t jdd�}|�d� d|j_tdd|d�}|�|d �}|�|d �}|j|d	d d �f d
d�}t�|||g�}t�ddg�}t�ddg�}	tj	g |	�d�R � }
tj	g |�d�R � }t�
|
|�\}}t�|�}t|jd �D ]-}t|jd	 �D ]#}t| ||| | || | �|||f< |||f dkr�d|||f< qxqod}d}t�| |�| }t| ||||d � t| |||d d� |d	 j||t�|�dddtd�}|d	 �d� |d	 jddd� |d	 jddd� |d	 �|� |d	 �|	� |d	 j||dtddd�}|d	 j||d	 �� d |d td!d"�}|d	 j||d	 � � d |d td!d"�}|d	 j!d#d$d%t"d&d'd(�d|d	 j#d)d)d*� |d j$|||t%d+d,d-� |d j&|||d.d/d0� t �'d1� t �(d2� |d j)�*d3� |d j+�,d4� |d j-�,d4� |d j)�,d4� |d j.d5d6d7� t j/d8dd9� |d �0d:d;� |||||gfS )<N)�	   rF   �rI   z#ffffff�topr%   )�figure)r   r   )r   r   r   �3d��
projectiong      Y���  g     @o�i^  rC   r   g�����ư>��   ����rK   rR   �ffffff�?)�levels�
linewidths�alpha�colorsz	Cost(w,b)r=   rD   rS   r>   �cost with 
current w,brL   rG   r'   rO   g      �?gffffff�?zClick to choose w,b�white�black)�	facecolor�ec�center)�bboxrT   r6   �verticalalignment�horizontalalignment�333333�?T��cmaprz   �antialiased�k皙�����?�r)   rz   �$w$�$b$F��      �?r�   r�   g        z	J(w, b)

�Z   ��rotationz(Cost(w,b) 
 [You can rotate this figure]��size�   ����)1r   rp   �set_facecolorrW   rX   r   �add_subplotrU   re   �linspace�meshgridrg   rh   �shaper   rV   rA   r$   �contour�logr   r   r   r   �set_xlim�set_ylimr   r   rY   rZ   r   r8   r[   r;   �dictr<   �plot_surface�dlcm�plot_wireframe�xlabel�ylabel�zaxis�set_rotate_label�xaxis�set_pane_color�yaxis�
set_zlabel�title�	view_init)rb   rc   r!   �gs�ax0�ax1�ax2r    ri   �b_rangeZb_spaceZw_spacer`   rk   �zrj   �j�w0r>   r   �CSZcscatZchlineZcvliner"   r"   r#   �plt_stationaryd   s^   

&��"&&�

r�   c                   @   s   e Zd Zdd� Zdd� ZdS )�plt_update_onclickc                 C   s2   || _ || _|| _|| _|| _|j�d| �| _d S )N�button_press_event)r!   r    rb   rc   �	dyn_itemsrW   �mpl_connect�cid)�selfr!   r    rb   rc   r�   r"   r"   r#   �__init__�   s   zplt_update_onclick.__init__c                 C   sr  |j | jd kr�|j}|j}t| j| j||�}| jd ��  t�	| j|�| }t
| j| j||| jd � t| j| j|| jd d� | jD ]}|��  qD| jd j||dtddd�}| jd j|| jd �� d |dtd	d
�}| jd j|| jd �� d |dtd	d
�}	| jd jd|d��||fddtdd�dd�}
| jd j|||ddd�}|||	|
|g| _| jj��  d S d S )Nr   r   rK   rC   rD   r|   rL   rG   r'   rO   zCost: z.0f)rG   rG   r.   r}   )r   )r/   r1   r2   r�   r�   r%   r   )r   rM   )�inaxesr    �xdata�ydatar   rb   rc   �clearrU   rV   rA   r$   r�   �remover   r   rY   rZ   r   r8   r[   r9   r�   �	scatter3Dr!   rW   �draw)r�   �event�ws�bs�cstr   �artist�ar>   r   �d�er"   r"   r#   �__call__�   s(   

**
��zplt_update_onclick.__call__N)�__name__�
__module__�__qualname__r�   r�   r"   r"   r"   r#   r�   �   s    r�   c                  C   sB  t jdd�} | jddd�}|j�d� |j�d� |j�d� |j�d� |�dd	� t	�
d
dd�}t	�
d
dd�}t	�t|�t|�f�}d}|D ]}d}|D ]}|d |d  |||f< |d7 }qN|d7 }qHt	�||�\}	}
|j|	|
|dddd� |j|	|
|ddd� |�d� |�d� |jddd� |jddd� t ��  dS )z, Create figure and plot with a 3D projection)rF   rF   rn   �o   rq   rr   r�   F�-   r�   i�����   rC   r   r%   r   Z
Spectral_rrw   r�   r�   r�   r�   r�   r�   z$J(w,b)$r�   r�   z&$J(w,b)$
 [You can rotate this figure]�   r�   N)r   rp   r�   r�   r�   r�   r�   r�   r�   rU   r�   �zerosr:   r�   r�   r�   r   r   r�   r   r]   )r!   r    r=   r>   r�   r�   r   rj   r   �W�Br"   r"   r#   �	soup_bowl�   s2   



r�   c                 C   sh   |\}}|\}}| \}}	|\}
}||kr2||k r2|
|kr2|
|k r2|	|kr2|	|k r2||kr2||k r2dS dS )NTFr"   )r�   r>   �xlim�ylimZxlow�xhighZylow�yhighr    �ay�bx�byr"   r"   r#   �inbounds�   s    ����r�   )rv   rt   r   )i���rt   r   )r�   �2   ��  i�  i'  i�a  iP�  ru   rC   rD   c                 C   s�  t �t j|� t j|� �\}}t �|�}t|jd �D ]}t|jd �D ]}t| ||| | || | �|| |< q#q|j||||dtt	t
ttgd�}|j|dddd� |�d� |�d	� |�d
� |}|	}|j||�� d |dtdd� |j||�� d |dtdd� |d }|dd |
� D ]@}t �|d |d  d |d |d  d  �}||ks�||d kr�t|||�� |�� �r�tjd||ddddd�ddd� |}q�d S )Nr   r   r%   )ry   r{   z%1.0frD   )�inline�fmtrT   r=   r>   zAContour plot of cost J(w,b), vs b,w with path of gradient descentr'   rO   r5   r+   r-   �->r   r&   )�
arrowstyler)   r(   r�   )r/   r1   r0   �
arrowprops�va�ha)rU   r�   rf   rg   rh   r�   r   r�   r   r   r	   r
   r   �clabelr   r   r   rY   rZ   r8   r[   �sqrtr�   r   r9   )r   r   �histr    ri   r�   �contours�
resolution�w_final�b_final�step�b0r�   r�   rj   r�   r�   r=   r>   �base�pointZedistr"   r"   r#   �plt_contour_wgrad�   s6   
(��
.
��r�   c                 C   sX  t �t| ��}t �t| ��}t �t| ��}tt| ��D ]}| | d ||< | | d ||< || ||< qtjdd�}tjdd� |�dd�}	|�d� |�	|	d d� �}
d	}t �
d
dd�}t �|�}tt|��D ]}|| }t||||�||< qh|
�||� |
j||td� |
�d� |
�d� |
�d� |
j�td�� t �t �
ddd�t �
d
dd��\}}t �|�}t|jd �D ]}t|jd �D ]}t|||| | || | �|| |< q�q�|j	|	dd � dd�}
|
j|||dtd� |
j�td�� |
j�td�� |
jddd� |
jddd� |
jddd� t�d� |
jddd� |
j|||td� d S ) Nr   r   )rR   r   rn   )�wspacer   z.Cost escalates when learning rate is too larger%   rC   i����ip r�   )r   zCost vs w, b set to 100rP   r=   iHw��i��  rt   rq   rr   r�   )rz   r)   �   rS   r>   z
costzCost vs (b, w)g      4@i����)�elev�azim)rU   r�   r:   rh   r   rp   �subplots_adjust�add_gridspecr\   r�   rf   rg   r   r   r
   r   r   r   r�   �set_major_locatorr   r�   r�   r�   r   r�   r�   r�   r�   )�p_hist�J_histrb   rc   r   r   �vrj   r!   r�   r    �fix_bra   r_   rk   r`   r�   r�   r"   r"   r#   �plt_divergence  sR   




$
(�
r  c                 C   s�   t �|| || d�}| ||  | }|j||tdd� |j||dtddd� |dkr-dnd}|jd	|  d
||fd|dfdtdd�ddd�	 d S )Nr�   )r)   rM   z--rD   r   )r   rN   �	linewidthru   r�   z#$\frac{\partial J}{\partial w}$ =%d�   r-   r.   r�   )r�   �leftro   )rT   r/   r0   r1   r2   r�   r�   r�   )rU   r�   r   r   r   r	   r9   r�   )Zdj_dx�x1�y1r�   r    r   r   �xoffr"   r"   r#   �add_lineU  s   
�r	  c              	   C   s  t jdddd�\}}d}t�ddd�}t�d	d
d�}t�|�}tt|��D ]}	||	 }
|| ||
|�||	< q%|d	 j||dd� |d	 �d� |d	 �	d� |d	 �
d� dD ]}
d}|| ||
|�\}}|| ||
|�}t||
|d|d	 � qVt�t�ddd�t�ddd��\}}
t�|
�}t�|�}t|
jd	 �D ]%}	t|
jd �D ]}|| ||
|	 | ||	 | �\||	 |< ||	 |< q�q�|
}|}d}t�|| d d || d d  �}|d �d� |d j|||||dd�}|d j|ddddddd� |d �
d� |d �	d� d S )Nr   r%   )rR   rG   rn   rC   rv   rt   r�   r   rB   )r  z&Cost vs w, with gradient; b set to 100rP   r=   )rC   ru   i,  r�   i8���ru   rD   iX  �����zGradient shown in quiver plot�width)�unitsg�������?z$2 \frac{m}{s}$�Erp   )�labelpos�coordinatesr>   )r   r   rU   r�   rg   rh   r:   r   r   r   r   r	  r�   r�   r�   �quiver�	quiverkey)rb   rc   Zf_compute_costZf_compute_gradientr!   r    r  ra   r_   rj   rk   �dj_dw�dj_dbr�   r`   �U�Vr   �Y�n�color_array�Qr"   r"   r#   �plt_gradientsa  s@   
$

4�& r  )NN)&�__doc__�numpyrU   �matplotlib.pyplot�pyplotr   �matplotlib.tickerr   �matplotlib.gridspecr   �matplotlib.colorsr   Z
ipywidgetsr   Zlab_utils_commonr   r   r   r	   r
   r   r   �style�useZn_bin�	from_listr�   r$   rA   rl   r�   r�   r�   r�   r�   r  r	  r  r"   r"   r"   r#   �<module>   s8     �
">&'

�>