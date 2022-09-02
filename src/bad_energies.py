class BadEnergies(pd.DataFrame): 
    meta = '' 
    
    def __init__(self, *args, **kwargs):
        return super(BadEnergies, self).__init__(*args, **kwargs)
    
    @property
    def _constructor(self):
        return BadEnergies
    
    def _get_top(self, n):
        data = self.copy()
        return list(
            data[[i for i in data.columns if i != 'anio']]
            .groupby('pais_iso')
            .mean()
            .sum(axis=1)
            .sort_values(ascending=False)
            .index[:n]
            .values
        )
    
    def _get_melt(self):
        return self.melt(
            id_vars=['pais_iso', 'anio'], 
            value_vars=filter(lambda x: x not in ['pais_iso', 'anio'], self.columns),
            value_name='valor', 
            var_name='tipo_energia'
        )
        
    def get_data(self, filt: T.Literal['cons', 'produccion']):
        BadEnergies.meta = filt
        bad_energies = [
            c 
            for c in self.columns 
            if (
                (
                   'gas' in c
                    or 'petroleo' in c
                    or 'carbon' in c
                    and not 'green' in c
                    and not 'low' in c
                )
            )
        ]
        data = self.copy()
        columns = [i for i in bad_energies if filt in i] + ['pais_iso', 'anio']
        data = data[columns]
        return data
    
    def plot_and_top(self, column, show=False):
        data = self.copy()
        col = column + '_' + self.meta
        fig = px.bar(top_carbon := (
            data[['pais_iso', col]]
            .groupby('pais_iso')
            .mean()
            .sort_values(col, ascending=False)
            .head(10)
        ))
        top_carbon_iso = top_carbon.index
        return fig, top_carbon_iso
    
    def fig_and_table(self, n=10):
        top = self._get_top(n)
        data = (
            self.copy()
            ._get_melt()
            .drop('anio', axis=1)
            .groupby(['pais_iso', 'tipo_energia'])
            .mean()
            .loc[top]
            .reset_index()
        )
        return px.bar(
            data,
            x='pais_iso',
            y='valor',
            color='tipo_energia'
        
        ), data
    
    
    def _get_year(self, year: int) -> pd.DataFrame:
        data = self.copy()
        return (
            data
            .loc[data.anio == year]
            .set_index('pais_iso')
            .loc[data._get_top(10)]
            .reset_index()
            .melt(id_vars=['pais_iso', 'anio'], value_name='valor', var_name='tipo_energia')
            .round(2)
        )
    
    def get_pct_change(self, one: int, two: int):
        data_one = self.copy()._get_year(one)
        data_two = self.copy()._get_year(two) 
        data_pct = data_two.merge(data_one, on=['pais_iso', 'tipo_energia'])
        data_pct['cambio_porcentual'] = (data_pct.valor_x - data_pct.valor_y) / data_pct.valor_y * 100
        return data_pct.round(2)
